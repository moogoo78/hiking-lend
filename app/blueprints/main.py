from datetime import datetime

from flask import (
    Blueprint,
    request,
    render_template,
    jsonify,
    redirect,
    url_for,
    flash,
)
from sqlalchemy import (
    or_,
    and_,
)

from app.database import session
from app.models import (
    Store,
    Lending,
    Entity,
)

main = Blueprint('main', __name__)


@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/lend', methods=['GET', 'POST'])
def lend_view():
    if request.method == 'GET':
        #store_list = Store.query.all()
        #return render_template('lend.html', store_list=store_list)
        return redirect(url_for('main.calendar_view'))

    elif request.method == 'POST':
        pickdate = request.form.get('pickdate', '')
        store_id = request.form.get('store', '')
        date_list = pickdate.split(' - ')
        if entity := Entity.find_free(store_id, True):
            entity.status = Entity.STATUS_CHOICES[1][0]

            lend = Lending(
                person=request.form.get('person', ''),
                phone=request.form.get('phone', ''),
                date_start=date_list[0],
                date_end=date_list[1],
                remarks=request.form.get('remarks', ''),
                store_id=int(store_id),
                entity_id=entity.id
            )
            session.add(lend)
            session.commit()

            flash('registered')

        return redirect(url_for('main.calendar_view'))


@main.route('/calendar', methods=['GET', 'POST'])
def calendar_view():
    if request.method == 'GET':
        # today = datetime.today()
        # cal_list = calendar.monthcalendar(today.year, today.month)

        # return render_template(
        #     'calendar.html',
        #     #cal_list=cal_list,
        #     year=today.year,
        #     month=today.month)        
        if key := request.args.get('store'):
            if store := Store.query.filter(Store.title==key).first():
                return render_template('calendar.html', store=store)
            else:
                return abort(404)
        else:
            store_list = Store.query.all()
            return render_template('calendar.html', stores=store_list)

    elif request.method == 'POST':
        pickdate = request.form.get('pickdate', '')
        date_list = pickdate.split(' - ')
        store_name = request.form.get('store', '')

        if len(date_list) < 2:
            return redirect(url_for('main.calendar_view'))

        lending_list = Lending.query.filter(or_(
            and_(date_list[0] >= Lending.date_start, date_list[0] <= Lending.date_end),
            and_(date_list[1] >= Lending.date_start, date_list[1] <= Lending.date_end),
            and_(date_list[0] <= Lending.date_start, date_list[1] >= Lending.date_end))
        ).all()
        stores = {}
        store_list = Store.query.all()
        for store in store_list:
            #print(len(store.entities), flush=True)
            stores[store.id] = {
                'num_entity': len(store.entities),
                'obj': store,
            }
        for i in lending_list:
            stores[i.store_id]['num_entity'] -= 1

        store_list = [stores[x]['obj'] for x in stores if stores[x]['num_entity'] > 0]
        #print(stores, flush=True)
        return render_template('lend.html', store_list=store_list, pickdate=pickdate, store_name=store_name)

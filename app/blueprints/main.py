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
from werkzeug.security import (
    check_password_hash,
)
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
)
from app.database import session
from app.models import (
    Store,
    Lending,
    Entity,
    User,
)
from app.helpers import send_email

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
        store_id = request.form.get('store_id', '')
        date_list = pickdate.split(' - ')

        if entity := Entity.find_free(store_id, True):
            if store := session.get(Store, entity.store_id):
                print(store.title, store.next_process, store_id, flush=True)
                if store.next_process == 'contact':
                    return render_template('show_contact.html', {'store': store})
                else: #if store.next_process == 'payment':
                    return render_template('payment.html')
                #entity.status = Entity.STATUS_CHOICES[1][0]
        '''
            lend = Lending(
                person=request.form.get('person', ''),
                phone=request.form.get('phone', ''),
                date_start=date_list[0],
                date_end=date_list[1],
                remarks=request.form.get('remarks', ''),
                store_id=entity.store_id,
                entity_id=entity.id
            )
            session.add(lend)
            session.commit()
        '''
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
        store_id = request.form.get('store_id', '')
        store_obj = None
        if store_id:
            store_obj = session.get(Store, store_id)

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
        return render_template('lend.html', store_list=store_list, pickdate=pickdate, store_id=store_id, store=store_obj)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username', '')
        passwd = request.form.get('passwd', '')

        if u := User.query.filter(username==username).first():
            if check_password_hash(u.passwd, passwd):
                login_user(u)
                flash('已登入')
                #next_url = flask.request.args.get('next')
                # is_safe_url should check if the url is safe for redirects.
                # See http://flask.pocoo.org/snippets/62/ for an example.
                #if not is_safe_url(next):
                #    return flask.abort(400)
                return redirect(url_for('admin.index'))

        flash('帳號或密碼錯誤')
        return redirect('/login')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if email := request.form.get('email'):
            body = 'verified:'
            #send_email(email, 'inreach租借-註冊', 'test')
            return email
    elif request.method == 'GET':
        return render_template('register.html')

@main.route('/payment_callback')
def payment_callback():
    return render_template('payment_result.html')

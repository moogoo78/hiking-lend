from datetime import datetime
import calendar

from flask import (
    Blueprint,
    request,
    render_template,
    jsonify,
    redirect,
    url_for,
    flash,
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
        store_list = Store.query.all()
        return render_template('lend.html', store_list=store_list)

    elif request.method == 'POST':
        date_list = request.form.get('pickdate', '')
        date_list = date_list.split(' - ')
        lend = Lending(
            person=request.form.get('person', ''),
            phone=request.form.get('phone', ''),
            date_start=date_list[0],
            date_end=date_list[1],
            remarks=request.form.get('remarks', ''),
        )
        session.add(lend)
        #session.commit()

        return redirect(url_for('main.calendar_view'))

@main.route('/calendar')
def calendar_view():
    today = datetime.today()
    cal_list = calendar.monthcalendar(today.year, today.month)

    return render_template(
        'calendar.html',
        cal_list=cal_list,
        year=today.year,
        month=today.month)

@main.route('/api/calendar/<year>/<month>')
def calendar_api(year, month):
    cal_list = calendar.monthcalendar(year, month)
    return jsonify({
        'year': year,
        'month': month,
        'cal_list': cal_list,
    })

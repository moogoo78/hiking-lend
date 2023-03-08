from datetime import datetime
import calendar

from flask import (
    Blueprint,
    request,
    jsonify,
)

from app.models import (
    Store,
    Lending,
    Entity,
)

api = Blueprint('api', __name__)


@api.route('/stores')
def get_stores():
    store_list = Store.query.all()
    return jsonify([x.to_dict() for x in store_list])

@api.route('/calendar/lended-dates')
def get_calendar():
    month_range = 2 # un-use

    dt = datetime.today()
    #dt = datetime.strptime('2023-12-01', '%Y-%m-%d')
    start_year = dt.year
    end_year = dt.year
    start_month = dt.month
    end_month = dt.month + 1
    if start_month == 12:
        end_year = end_year + 1
        end_month = 1

    start_date = datetime.strptime(f'{start_year}-{start_month}-01', '%Y-%m-%d')
    end_month_range = calendar.monthrange(end_year, end_month)
    end_date = datetime.strptime(f'{end_year}-{end_month}-{end_month_range[1]}', '%Y-%m-%d')

    dates = {}
    for i in range(calendar.monthrange(start_year, start_month)[1]):
        k = datetime(start_year, start_month,i+1).strftime('%Y-%m-%d')
        dates[k] = 0

    for i in range(calendar.monthrange(end_year, end_month)[1]):
        k = datetime(end_year, end_month,i+1).strftime('%Y-%m-%d')
        dates[k] = 0

    lended = Lending.query.filter(Lending.date_start >= start_date ,Lending.date_end <= end_date).all()
    for i in lended:
        for k in dates:
            d = datetime.strptime(k, '%Y-%m-%d').date()
            if d >= i.date_start and d <= i.date_end:
                dates[k] += 1

    total_entity= Entity.query.count()
    booked_full = []
    booked_some = []
    for k in dates:
        if dates[k] == total_entity:
            booked_full.append(k)
        elif dates[k] > 0:
            booked_some.append(k)

    # [[x.date_start.strftime('%Y-%m-%d'), x.date_end.strftime('%Y-%m-%d')] for x in lended],
    return jsonify({
        'range': [start_date, end_date],
        'booked_full': booked_full,
        'booked_some': booked_some,
    })

@api.route('/calendar/<year>/<month>')
def get_calendar_deprecated(year, month):
    cal_list = calendar.monthcalendar(year, month)
    return jsonify({
        'year': year,
        'month': month,
        'cal_list': cal_list,
    })

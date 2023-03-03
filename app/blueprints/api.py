from flask import (
    Blueprint,
    request,
    jsonify,
)

from app.models import (
    Store,
)

api = Blueprint('api', __name__)


@api.route('/stores')
def get_stores():
    store_list = Store.query.all()
    return jsonify([x.to_dict() for x in store_list])

@api.route('/calendar/<year>/<month>')
def get_calendar(year, month):
    cal_list = calendar.monthcalendar(year, month)
    return jsonify({
        'year': year,
        'month': month,
        'cal_list': cal_list,
    })

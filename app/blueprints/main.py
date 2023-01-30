from flask import (
    Blueprint,
    request,
    render_template,
    jsonify,
)

from app.database import session

main = Blueprint('main', __name__)


@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/lend')
def lend():
    return render_template('lend.html')

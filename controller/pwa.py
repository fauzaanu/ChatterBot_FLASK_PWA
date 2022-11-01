from flask import (
    Blueprint, make_response, send_from_directory
)

bp = Blueprint('pwa', __name__, url_prefix='')


@bp.route('/app.webmanifest')
def manifest():
    return send_from_directory('static', 'app.webmanifest')


@bp.route('/serviceworker.js')
def service_worker():
    response = make_response(send_from_directory('static', 'serviceworker.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response
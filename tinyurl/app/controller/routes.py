from flask import render_template, request, flash, redirect, url_for, abort, g, jsonify, Blueprint
from redis import Redis
from config.config import config

bp = Blueprint('tinyurl', __name__)

redis_conf = config.REDIS

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host=redis_conf['HOST'], db=redis_conf['DB_ID'], socket_timeout=redis_conf['SOCKET_TIMEOUT'])
    return g.redis


@bp.route('/health')
def healthcheck():
    return jsonify({"status": "Up"}), 200


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/your_url', methods=['POST'])
def your_url():
    redis = get_redis()

    if request.method == 'POST':
        key = request.form['tinyurl']

        if redis.get(key):
            flash('Short name already exist, Try a different short name')
            return redirect(url_for('tinyurl.home'))

        redis.set(key, request.form['url'])

        return render_template('your_url.html', tinyurl=request.form['tinyurl'], full_url=request.form['url'])


@bp.route('/<string:tinyurl>')
def redirect_to_url(tinyurl):
    redis = get_redis()
    site_url = redis.get(tinyurl)
    if site_url:
        return redirect(site_url)
    return abort(404)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

from flask import Flask, render_template, request, flash, redirect, url_for, abort, g, Response, jsonify
from redis import Redis

app = Flask(__name__)
app.secret_key = "dummysecret"


def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis

@app.route('/health')
def healthcheck():
    return jsonify({"status": "Up"}),200

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your_url', methods=['GET', 'POST'])
def your_url():
    redis = get_redis()

    if request.method == 'POST':
        key = request.form['tinyurl']

        if redis.get(key):
            flash('Short name already exist, Try a different short name')
            return redirect(url_for('home'))

        redis.set(key, request.form['url'])

        return render_template('your_url.html', tinyurl=request.form['tinyurl'], full_url=request.form['url'])


@app.route('/<string:tinyurl>')
def redirect_to_url(tinyurl):
    redis = get_redis()
    site_url = redis.get(tinyurl)
    if site_url:
        return redirect(site_url)
    return abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

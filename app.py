from flask import Flask, render_template, request, flash, redirect, url_for, abort
import json
import os.path

app = Flask(__name__)
app.secret_key = "dummysecret"

url_file_path = os.getcwd()


def get_urls_dict():
    urls = {}
    if os.path.exists(url_file_path + '/urls.json'):
        with open('urls.json', 'r') as url_file:
            urls = json.load(url_file)
    return urls


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your_url', methods=['GET', 'POST'])
def your_url():
    urls = {}
    if request.method == 'POST':
        key = request.form['tinyurl']

        urls = get_urls_dict()

        if key in urls.keys():
            flash('Short name already exist, Try a different short name')
            return redirect(url_for('home'))

        with open('urls.json', 'w') as url_file:
            urls[key] = {'url': request.form['url']}
            json.dump(urls, url_file)

        return render_template('your_url.html', tinyurl=request.form['tinyurl'], full_url=request.form['url'])


@app.route('/<string:tinyurl>')
def redirect_to_url(tinyurl):
    urls = get_urls_dict()
    if tinyurl in urls.keys():
        return redirect(urls[tinyurl]['url'])
    return abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

from flask import Flask, request, render_template, jsonify
from utils import *
import json

app = Flask(__name__, template_folder='templates')


@app.route('/')
def page_index():
    posts = get_all_inf()
    return render_template("index.html", posts=posts)



# @app.route('/users/<data>')
# def get_user_name(data):
#     posts = get_posts_by_user(data)
#     return render_template("index.html", posts=posts)


@app.route("/search/")
def page_tag():
    s = request.args.get('s', "")
    posts = subject(s)
    return render_template("index.html", s=s, posts=posts)


@app.errorhandler(404)
def error_404(e):
    return 'Такое не найдено', 404

@app.errorhandler(500)
def error_500(e):
    return'Internal Server Error ', 500

@app.route('/api/post')
def api_posts():
    posts = get_all_inf()
    return jsonify(posts)

@app.route('/api/post/<data>')
def api_post(data):
    post = get_dates(data)
    return jsonify(post)

app.run()




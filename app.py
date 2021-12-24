from flask import Flask, render_template, request, url_for
from PIL import Image
app = Flask(__name__)
FLASK_RUN_PORT = 8000

# @app.route('/favicon.ico')
# def favicon():
#     img = Image.open('favicon.ico')
#     return img


@app.route('/bootstrap_example')
def home_bootstrap_func():
    return render_template('bootstrap_home.html')


@app.route('/')
def home_func():
    users = [
        {'id': 1, 'name': 'Ariel', 'last': 'Koen', 'email': 'a@a.a'},
        {'id': 2, 'name': 'bob', 'last': 'a', 'email': 'a@a.a'},
        {'id': 3, 'name': 'bab', 'last': 'b', 'email': 'b@a.a'},
        {'id': 4, 'name': 'bib', 'last': 'c', 'email': 'c@a.a'},
    ]
    return render_template('home_for_web_lectures.html', users=users)


if __name__ == '__main__':
    app.run(port=5001, debug=True)

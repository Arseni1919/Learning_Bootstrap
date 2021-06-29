from flask import Flask, render_template, request, url_for
from PIL import Image
app = Flask(__name__)


# @app.route('/favicon.ico')
# def favicon():
#     img = Image.open('favicon.ico')
#     return img


@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

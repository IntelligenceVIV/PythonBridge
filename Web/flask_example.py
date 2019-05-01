# @Time    : 2019/4/18 2:46
# @Author  : Noah
# @File    : flask_demo.py
# @Software: PyCharm
# @description: simple flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run()

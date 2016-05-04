# -*- coding:utf-8 -*-

import os
from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.append(BASE_DIR + "/views")


@route("/")
@route("/index")
def hello():
    return template("index", message="Hello World!!!!!!")


@route("/insert")
def insert():
    return template("insert", message="hoge")


@route("/select")
def select():
    return template("select", message="select")


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

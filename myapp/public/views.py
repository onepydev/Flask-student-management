from flask import Blueprint, render_template,url_for,request
from myapp.appclass.api import apiuser


publicview=Blueprint("publicview",__name__)


@publicview.route("/",methods=['GET'])
def index():
    message="Welcome to my first Flask strutured App"

    return render_template("public/","Email Confirmation Status",message=message)
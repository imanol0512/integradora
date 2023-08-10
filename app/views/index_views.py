from flask import render_template,Blueprint

index_views=Blueprint('index',__name__)

@index_views.route("/")
def index():
    return render_template('index/index.html')

@index_views.route("/index/indexadmin/")
def indexadmin():
    return render_template('index/indexadmin.html')

@index_views.route("/index/indexcajero")
def indexcajero():
    return render_template('index/indexcajero.html')
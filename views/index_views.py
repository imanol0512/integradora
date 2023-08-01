from flask import render_template,Blueprint

index_views=Blueprint('index',__name__)

@index_views.route("/")
def index():
    return render_template('index/index.html')
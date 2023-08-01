from flask import render_template,Blueprint

error_views=Blueprint('error',__name__)

@error_views.app_errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html')
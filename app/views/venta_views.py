from flask import render_template,redirect,url_for,Blueprint
from models.venta import Venta
from models.detallesventa import DetallesVenta

venta_views=Blueprint('venta',__name__)

@venta_views.route("/ventas/")
def ventas():
    ventas=Venta.get_all()
    return render_template('venta/ventas.html',ventas=ventas)
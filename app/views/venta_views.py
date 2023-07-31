from flask import render_template,redirect,url_for,Blueprint
from models.venta import Venta
from models.detallesventa import DetallesVenta
from models.articulo import Articulo
from forms.detalles_forms import CantForm

venta_views=Blueprint('venta',__name__)

@venta_views.route("/ventas/")
def ventas():
    ventas=Venta.get_all()
    return render_template('venta/ventas.html',ventas=ventas)

@venta_views.route("/venta/<int:idventa>")
def detalles(idventa):
    detalles=DetallesVenta.get(idventa)
    return render_template('venta/detalles_venta.html',detalles=detalles)

@venta_views.route("/venta/nueva/")
def crear_venta():
    detalles=DetallesVenta.get_all_new()
    return render_template("venta/crear_venta.html",detalles=detalles)

def insertar_articulo():
    articulos=Articulo.get_all()

def insertar_cantidad(idarticulo):
    form=CantForm()
    detalles=DetallesVenta.get_new(idarticulo)

    if form.validate_on_submit():
        detalles.cantidad=form.cantidad.data
        detalles.save()
        return redirect(url_for('venta.nueva'))
    form.cantidad.data=detalles.cantidad
    return render_template("venta/crear_venta.html",form=form,detalles=detalles)

def eliminar_articulo(idarticulo):
    detalles=DetallesVenta.get_new(idarticulo)
    detalles.delete_new()
    return redirect(url_for("venta.ventas"))

def cancelar_venta():
    DetallesVenta.cancel()
    return redirect(url_for("venta.ventas"))
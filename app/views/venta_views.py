from flask import render_template,redirect,url_for,Blueprint
from models.venta import Venta
from models.usuario import Usuario
from models.detallesventa import DetallesVenta,VistaDetalles
from models.articulo import Articulo
from forms.detalles_forms import CantForm

venta_views=Blueprint('venta',__name__)

@venta_views.route("/ventas/")
def ventas():
    ventas=Venta.get_all()
    return render_template('venta/ventas.html',ventas=ventas)

@venta_views.route("/venta/<int:idventa>")
def detalles(idventa):
    venta=Venta.get(idventa)
    total=DetallesVenta.total_consulta(idventa)
    return render_template('venta/detalles_venta.html',venta=venta,total=total)

@venta_views.route("/venta/nueva/")
def crear_venta():
    detalles=VistaDetalles.get_all_new()
    return render_template("venta/crear_venta.html",detalles=detalles)

def eliminar_articulo(idarticulo):
    detalles=DetallesVenta.get_new(idarticulo)
    detalles.delete_new()
    return redirect(url_for("venta.ventas"))

def registrar_venta():
    venta=Venta.save()
    articulos=DetallesVenta.registrar_venta()
    return redirect(url_for("venta.ventas",venta=venta,articulos=articulos))


def cancelar_venta():
    DetallesVenta.cancel()
    return redirect(url_for("venta.ventas"))

@venta_views.route("/venta/nueva/articulos/")
def consulta_articulos():
    articulos=Articulo.get_all()
    return render_template('venta/insert_art.html',articulos=articulos)

@venta_views.route("/venta/articulos/<int:id>/cantidad/")
def insertar_cantidad(idarticulo):
    form=CantForm()
    art=Articulo.__get__(idarticulo)
    detalles=DetallesVenta.get_new(idarticulo)

    if form.validate_on_submit():
        detalles.cantidad=form.cantidad.data
        detalles.save()
        return redirect(url_for('venta.nueva'))
    form.cantidad.data=detalles.cantidad
    return render_template("venta/cantidad.html",form=form,detalles=detalles,art=art)


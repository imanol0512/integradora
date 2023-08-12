from flask import render_template,redirect,url_for,Blueprint
from models.venta import Venta
from models.usuario import Usuario
from models.detallesventa import DetallesVenta
from models.articulo import Articulo
from forms.detalles_forms import CantForm

venta_views=Blueprint('venta',__name__)

@venta_views.route("/ventas/")
def ventas():
    ventas=Venta.get_all()
    return render_template('venta/ventas.html',ventas=ventas)

@venta_views.route("/venta/<int:idventa>")
def detalles(idventa,idarticulo):
    venta=Venta.get(idventa)
    detalles=DetallesVenta.get(idventa)
    subtotal=DetallesVenta.subtotal_consulta(idventa,idarticulo)
    total=DetallesVenta.total_consulta(idventa)
    return render_template('venta/detalles_venta.html',venta=venta,detalles=detalles,subtotal=subtotal,total=total)

@venta_views.route("/venta/nueva/")
def crear_venta():
    detalles=DetallesVenta.get_all_new()
    subtotal=DetallesVenta.subtotal_new()
    total=DetallesVenta.total_new()
    return render_template("venta/crear_venta.html",detalles=detalles,subtotal=subtotal,total=total)

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

def insertar_articulo(id):
    articulo=Articulo.__get__(id)
    artVenta=DetallesVenta.get_one(articulo.id)
    artVenta=DetallesVenta.save()
    return render_template('venta/crear_venta.html',artVenta=artVenta)

def insertar_cantidad(idarticulo):
    form=CantForm()
    detalles=DetallesVenta.get_new(idarticulo)

    if form.validate_on_submit():
        detalles.cantidad=form.cantidad.data
        detalles.save()
        return redirect(url_for('venta.nueva'))
    form.cantidad.data=detalles.cantidad
    return render_template("venta/crear_venta.html",form=form,detalles=detalles)


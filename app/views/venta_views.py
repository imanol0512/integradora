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
    detalles=DetallesVenta.get(idventa)
    total=DetallesVenta.total_consulta(idventa)
    return render_template('venta/detalles_venta.html',
                           venta=venta,
                           total=total,
                           detalles=detalles['articulosVenta'],
                           subtotales=detalles['subtotales'], size_result=len(detalles['subtotales']))

@venta_views.route("/venta/nueva/")
def crear_venta():
    detalles=VistaDetalles.get_all_new()
    total=DetallesVenta.total_new()
    return render_template("venta/crear_venta.html",detalles=detalles,total=total)

def eliminar_articulo(idarticulo):
    detalles=DetallesVenta.get_new(idarticulo)
    detalles.delete()
    return redirect(url_for("venta.ventas"))

@venta_views.route("/venta/registrar/",methods=['POST'])
def registrar_venta():
    venta=Venta.registrar_venta()
    return render_template("venta/venta_exitosa.html",venta=venta)

@venta_views.route("/venta/cancelar/",methods=['POST'])
def cancelar_venta():
    DetallesVenta.cancel()
    return render_template("venta/venta_cancelada.html")

@venta_views.route("/venta/nueva/articulos/")
def consulta_articulos():
    articulos=Articulo.get_all()
    return render_template('venta/insert_art.html',articulos=articulos)

@venta_views.route("/venta/articulos/<int:id>/cantidad/",methods=['GET','POST'])
def insertar_cantidad(id):    
    form=CantForm()
    art=Articulo.__get__(id)
    if form.validate_on_submit():
        idventa=''
        idarticulo=art.id
        cantidad=form.cantidad.data
        detalles=DetallesVenta(idventa,idarticulo,cantidad)
        detalles.save()
        return redirect(url_for('venta.crear_venta'))
    return render_template("venta/cantidad.html",form=form,art=art)

@venta_views.route('/venta/articulos/<nombre>/cantidad/actualizar',methods=['GET','POST'])
def actualizar_art(nombre):
    form=CantForm()
    idarticulo=VistaDetalles.get_new_id(nombre)
    art=Articulo.__get__(idarticulo)
    detalles=DetallesVenta.get_new_with_id(idarticulo)
    if form.validate_on_submit():
        detalles.cantidad=form.cantidad.data
        detalles.update()
        return redirect(url_for('venta.crear_venta'))
    form.cantidad.data=detalles.cantidad
    return render_template("venta/cantidad.html",form=form,art=art)

@venta_views.route('/venta/articulos/<nombre>/eliminar',methods=['POST'])
def eliminar_art(nombre):
    idarticulo=VistaDetalles.get_new_id(nombre)
    detalles=DetallesVenta.get_new_with_id(idarticulo)
    if detalles:
        detalles.delete()
        return redirect(url_for('venta.crear_venta'))
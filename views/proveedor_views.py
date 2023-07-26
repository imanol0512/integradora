from flask import render_template, redirect, url_for, Blueprint
from models.proveedor import Proveedor
from forms.proveedor_forms import CreateProvForm, UpdateProvForm

proveedor_views = Blueprint('proveedor', __name__)

@proveedor_views.route("/proveedores/")
def proveedores():
    # Consultar proveedores de BD
    proveedores = Proveedor.get_all()
    return render_template('proveedor/proveedores.html', proveedores=proveedores)

@proveedor_views.route("/proveedor/nuevo/", methods=('GET', 'POST'))
def crear_prov():
    form = CreateProvForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        telefono = form.telefono.data
        direccion = form.direccion.data
        numdireccion = form.numdireccion.data
        colonia = form.colonia.data
        municipio = form.municipio.data
        estado = form.estado.data
        prov = Proveedor(nombre, apellido, telefono, direccion, numdireccion, colonia, municipio, estado)
        prov.save()
        return redirect(url_for('proveedor.proveedores'))
    return render_template('proveedor/crear_prov.html', form=form)

@proveedor_views.route("/proveedor/<int:id>/actualizar/", methods=('GET', 'POST'))
def actualizar_prov(id):
    form = UpdateProvForm()
    prov = Proveedor.get(id)
    if form.validate_on_submit():
        prov.nombre = form.nombre.data
        prov.apellido = form.apellido.data
        prov.telefono = form.telefono.data
        prov.direccion = form.direccion.data
        prov.numdireccion = form.numdireccion.data
        prov.colonia = form.colonia.data
        prov.municipio = form.municipio.data
        prov.estado = form.estado.data
        prov.save()
        return redirect(url_for('proveedor.proveedores'))
    form.nombre.data = prov.nombre
    form.apellido.data = prov.apellido
    form.telefono.data = prov.telefono
    form.direccion.data = prov.direccion
    form.numdireccion.data = prov.numdireccion
    form.colonia.data = prov.colonia
    form.municipio.data = prov.municipio
    form.estado.data = prov.estado
    return render_template('proveedor/crear_prov.html', form=form)

@proveedor_views.route("/proveedor/<int:id>/eliminar/", methods=('POST',))
def eliminar_prov(id):
    prov = Proveedor.get(id)
    prov.delete()
    return redirect(url_for('proveedor.proveedores'))

# Nueva ruta para el botón de regresar
@proveedor_views.route("/proveedor/regresar/")
def regresar():
    return redirect(url_for('proveedor.proveedores'))

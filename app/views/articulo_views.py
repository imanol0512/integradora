from flask import render_template, redirect, url_for, Blueprint
from models.articulo import Articulo
from models.categoria import Categoria
from forms.articulo_forms import CreateArtForm, UpdateArtForm
from utils.file_handler import save_image

articulo_views = Blueprint('articulo', __name__)

@articulo_views.route("/articulos/")
def articulos():
    # Consultar artículos en BD:
    articulos = Articulo.get_all()
    return render_template('articulo/articulos.html', articulos=articulos)

@articulo_views.route("/articulos/categoria/")
def categorias():
   #Consultar artículos por su categoría
   categorias=Categoria.get_all()
   return render_template("articulo/categorias.html",categorias=categorias)

@articulo_views.route("/articulos/categoria/<int:id>")
def articulos_por_categoria(categoria):
    cat=Categoria.get(categoria)
    articulos=Articulo.get_by_cat(cat)
    return render_template("articulo/articulos.html",articulos=articulos)

@articulo_views.route("/articulo/nuevo/", methods=('GET', 'POST'))
def crear_art():
    form = CreateArtForm()
    if form.validate_on_submit():
        cb = form.cb.data
        nombre = form.nombre.data
        precio = form.precio.data
        marca = form.marca.data
        categoria = form.categoria.data
        existencias = form.existencias.data
        art = Articulo(cb, nombre, precio, marca, categoria, existencias)
        art.save()
        return redirect(url_for('articulo.articulos'))
    return render_template('/articulo/crear_art.html', form=form)

@articulo_views.route("/articulo/<int:id>/actualizar/", methods=('GET', 'POST'))
def actualizar_art(id):
    form = UpdateArtForm()
    art = Articulo.__get__(id)
    if form.validate_on_submit():
        art.cb = form.cb.data
        art.nombre = form.nombre.data
        art.precio = form.precio.data
        art.marca = form.marca.data
        art.categoria = form.categoria.data
        art.existencias = form.existencias.data
        f=form.image.data
        if f:
            art.image=save_image(f,'img/articulos',art.nombre)
        art.save()
        return redirect(url_for('articulo.articulos'))
    form.cb.data = art.cb
    form.nombre.data = art.nombre
    form.precio.data = art.precio
    form.marca.data = art.marca
    form.categoria.data = art.categoria
    form.existencias.data = art.existencias
    form.image.data=art.image
    return render_template('articulo/crear_art.html', form=form)

@articulo_views.route("/articulo/<int:id>/eliminar/",methods=('POST',))
def eliminar_art(id):
    art=Articulo.__get__(id)
    art.delete()
    return redirect(url_for('articulo.articulos'))
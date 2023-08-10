from flask import render_template, redirect, url_for, Blueprint, abort
from models.articulo import Articulo
from models.categoria import Categoria
from models.usuario import Usuario
from forms.articulo_forms import CreateArtForm, UpdateArtForm
from utils.file_handler import save_image

def configure_csrf(app):
    csrf = CsrfProtect(app)
    
articulo_views = Blueprint('articulo', __name__)

@articulo_views.route("/articulos/")
@articulo_views.route("/articulos/<int:pag>")
def articulos(pag=1):
    # Consultar artículos en BD:
    limite=20
    articulos = Articulo.get_all(limite=limite,pag=pag)
    totalArt=Articulo.count_all()
    pags=round(totalArt // limite,ndigits=0)
    form = UpdateArtForm()  # Crear una instancia del formulario UpdateArtForm
    return render_template('articulo/articulos.html', articulos=articulos, pags=pags, form=form)

@articulo_views.route("/articulos/categoria/")
def categorias():
   #Consultar artículos por su categoría
   categorias=Categoria.get_all()
   return render_template("articulo/categorias.html",categorias=categorias)

@articulo_views.route("/articulos/categoria/<int:id>")
@articulo_views.route("/articulos/categoria/<int:id>/<int:pag>")
def articulos_por_categoria(categoria):
    limite=20
    cat=Categoria.get(categoria)
    articulos=Articulo.get_by_cat(cat)
    totalArt=Articulo.count_all()
    pags=round(totalArt // limite,ndigits=0)
    return render_template("articulo/articulos.html",articulos=articulos,pags=pags)

@articulo_views.route("/articulo/nuevo/", methods=('GET', 'POST'))
def crear_art():
    form = CreateArtForm()
    cats=Categoria.get_all()
    categorias=[(-1,'')]
    for cat in cats:
        categorias.append((cat.id,cat.nombre))
    form.categoria.choices=categorias
    if form.validate_on_submit():
        cb = form.cb.data
        nombre = form.nombre.data
        precio = form.precio.data
        marca = form.marca.data
        categoria = form.categoria.data
        existencias = form.existencias.data
        f=form.image.data
        image=""
        if f:
            image=save_image(f,'img/articulos')
        art = Articulo(cb=cb,
                       nombre=nombre,
                       precio=precio,
                       marca=marca,
                       categoria=categoria,
                       existencias=existencias,
                       image=image)
        art.save()
        return redirect(url_for('articulo.articulos'))
    return render_template('/articulo/crear_art.html', form=form)

@articulo_views.route("/articulo/<int:id>/actualizar/", methods=('GET', 'POST'))
def actualizar_art(id):
    form = UpdateArtForm()
    cats=Categoria.get_all()
    categorias=[(-1,'')]
    for cat in cats:
        categorias.append((cat.id,cat.nombre))
    form.categoria.choices=categorias
    art = Articulo.__get__(id)
    if art is None:
        abort(404)
    if form.validate_on_submit():
        art.cb = form.cb.data
        art.nombre = form.nombre.data
        art.precio = form.precio.data
        art.marca = form.marca.data
        art.categoria = form.categoria.data
        art.existencias = form.existencias.data
        f=form.image.data
        if f:
            image=save_image(f,'img/articulos')
            art.image=image
        art.save()
        return redirect(url_for('articulo.articulos'))
    form.cb.data = art.cb
    form.nombre.data = art.nombre
    form.precio.data = art.precio
    form.marca.data = art.marca
    form.categoria.data = art.categoria
    form.existencias.data = art.existencias
    image=art.image
    return render_template('articulo/crear_art.html', form=form,image=image)

@articulo_views.route("/articulo/<int:id>/eliminar/",methods=('POST',))
def eliminar_art(id):
    art=Articulo.__get__(id)
    art.delete()
    return redirect(url_for('articulo.articulos'))
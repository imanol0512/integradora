<<<<<<< HEAD
from flask import Flask

#importar vistas
from views.articulo_views import articulo_views
from views.error_views import error_views
from views.proveedor_views import proveedor_views
from views.usuario_views import usuario_views

app=Flask(__name__)
app.config['SECRET_KEY']='my secret key'

app.register_blueprint(articulo_views)
app.register_blueprint(error_views)
app.register_blueprint(proveedor_views)
app.register_blueprint(usuario_views)
=======
from flask import Flask, render_template, request, redirect, url_for
from models.proveedor import Proveedor
from models.db import get_connection

app = Flask(__name__, static_folder='static')

# Simulación de datos de inicio de sesión (solo para propósito de demostración)
USUARIO_VALIDO = {'email': 'usuario@example.com', 'password': 'secreto'}

# Ruta para mostrar la tabla de proveedores
@app.route('/proveedores')
def lista_proveedores():
    # Obtener la lista de proveedores desde la base de datos
    proveedores = Proveedor.get_all()
    return render_template('indexproveedores.html', proveedores=proveedores)

# Ruta para mostrar el formulario de agregar proveedor
@app.route('/agregar_proveedor', methods=['GET', 'POST'])
def agregar_proveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        numdireccion = request.form['numdireccion']
        colonia = request.form['colonia']
        municipio = request.form['municipio']
        estado = request.form['estado']

        # Crear un nuevo objeto Proveedor y guardarlo en la base de datos
        nuevo_proveedor = Proveedor(nombre, apellido, telefono, direccion, numdireccion, colonia, municipio, estado)
        nuevo_proveedor.save()

        # Redireccionar a la página de proveedores después de guardar el nuevo proveedor
        return redirect(url_for('lista_proveedores'))

    return render_template('agregar_proveedor.html')
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339

# Resto del código de las rutas y funciones

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339

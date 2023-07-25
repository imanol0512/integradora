from flask import Flask, render_template, request, redirect, url_for

from models.proveedores import Proveedor

app = Flask(__name__)

# Simulación de datos de inicio de sesión (solo para propósito de demostración)
USUARIO_VALIDO = {'email': 'usuario@example.com', 'password': 'secreto'}

@app.route('/')
def index():
    mensaje = "Bienvenido al sitio web"
    return render_template('index.html', mensaje=mensaje)

@app.route('/catalogo_productos')
def catalogo_productos():
    # Datos de ejemplo para el catálogo de productos
    productos = [
        {
            'nombre': 'Producto 1',
            'precio': 10.99,
            'stock': 5,
            'imagen': 'producto1.jpg'
        },
        {
            'nombre': 'Producto 2',
            'precio': 15.99,
            'stock': 10,
            'imagen': 'producto2.jpg'
        },
        # Agregar más productos aquí si es necesario
    ]
    # Aquí puedes realizar cualquier procesamiento necesario antes de mostrar la página
    return render_template('catalogoproducto.html', productos=productos)

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == USUARIO_VALIDO['email'] and password == USUARIO_VALIDO['password']:
            return redirect(url_for('sesion_admin'))

    return render_template('inicioSesion.html')

@app.route('/sesion_admin', methods=['GET', 'POST'])
def sesion_admin():
    return render_template('indexadmin.html')

@app.route('/proveedores')
def lista_proveedores():
    # Obtener la lista de proveedores desde la base de datos
    proveedores = Proveedor.get_all()
    return render_template('index.html', proveedores=proveedores)

@app.route('/agregar_proveedor')
def agregar_proveedor():
    return render_template('agregar_proveedor.html')

if __name__ == '__main__':
    app.run(debug=True)


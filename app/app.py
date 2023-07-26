from flask import Flask

#importar vistas
from views.index_views import index_views
from views.articulo_views import articulo_views
from views.error_views import error_views
from views.proveedor_views import proveedor_views
from views.usuario_views import usuario_views

app=Flask(__name__)
app.config['SECRET_KEY']='my secret key'

app.register_blueprint(index_views)
app.register_blueprint(articulo_views)
app.register_blueprint(error_views)
app.register_blueprint(proveedor_views)
app.register_blueprint(usuario_views)

# Resto del código de las rutas y funciones

if __name__ == '__main__':
    app.run(debug=True)

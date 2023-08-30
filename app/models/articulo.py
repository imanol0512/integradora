from .db import get_connection

mydb=get_connection()

class Articulo:

    def __init__(self,cb,nombre,precio,marca,categoria,existencias,image='',id=None):
        self.id=id
        self.cb=cb
        self.nombre=nombre
        self.precio=precio
        self.marca=marca
        self.categoria=categoria
        self.existencias=existencias
        self.image=image

    def save(self):
        #Creación de nuevo objeto a DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql="INSERT INTO articulo(cb,nombre,precio,marca,categoria,existencias,image) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                val=(self.cb,self.nombre,self.precio,self.marca,self.categoria,self.existencias,self.image)
                cursor.execute(sql,val)
                mydb.commit()
                self.id=cursor.lastrowid
                return self.id
        #Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql="UPDATE articulo SET cb = %s,nombre = %s,precio = %s,marca = %s, categoria = %s, existencias = %s, image = %s WHERE id = %s"
                val=(self.cb,self.nombre,self.precio,self.marca,self.categoria,self.existencias,self.image,self.id)
                cursor.execute(sql,val)
                mydb.commit()
                return self.id
            
    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM articulo WHERE id={self.id}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.id
            
    #Selección
    @staticmethod
    def __get__(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT articulo.cb,articulo.nombre,articulo.precio,articulo.marca,categoria.nombre as 'categoria',articulo.existencias,image FROM articulo inner join categoria on categoria.id=articulo.categoria WHERE articulo.id={id}"
            cursor.execute(sql)
            art=cursor.fetchone()
            if art:
                art=Articulo(cb=art["cb"],
                             nombre=art["nombre"],
                             precio=art["precio"],
                             marca=art["marca"],
                             categoria=art["categoria"],
                             existencias=art["existencias"],
                             image=art["image"],
                             id=id)
                return art
            return None


    #Consulta por categoría
    @staticmethod
    def get_by_cat(categoria):
        articulos=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT cb,articulo.nombre,articulo.precio,articulo.marca,categoria.nombre as 'categoria',existencias FROM articulo where categoria={categoria}"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulos.append(Articulo(item["cb"],item["nombre"],item["precio"],item["marca"],item["categoria"],item["existencias"],item["image"]))
            return articulos

    #Consulta    
    @staticmethod
    def get_all():
        articulos=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT articulo.id,cb,articulo.nombre,articulo.precio,articulo.marca,categoria.nombre as 'categoria',articulo.existencias,image FROM articulo inner join categoria on categoria.id=articulo.categoria"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulos.append(Articulo(item["cb"],item["nombre"],item["precio"],item["marca"],item["categoria"],item["existencias"],item["image"],item["id"]))
            return articulos

    #Consulta para ventas (Evita que se pueda elegir el mismo artículo más de una vez ocultándolo de la selección)
    def get_for_sale():
        articulos=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT DISTINCT articulo.id,articulo.cb,articulo.nombre,articulo.precio,articulo.marca,categoria.nombre as categoria,articulo.existencias,articulo.image FROM articulo INNER JOIN categoria ON categoria.id=articulo.categoria INNER JOIN detallesventa ON articulo.id=detallesventa.idArticulo WHERE articulo.id NOT IN (SELECT idArticulo FROM detallesventa WHERE idVenta IS NULL)"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulos.append(Articulo(item["cb"],item["nombre"],item["precio"],item["marca"],item["categoria"],item["existencias"],item["image"],item["id"]))
            mydb.commit()
            cursor.close()
            return articulos

    #Contar
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql=f"SELECT COUNT(id) as total FROM articulo"
            cursor.execute(sql)
            result=cursor.fetchone()
            return result[0]

    #Validar nombre usuario
    def check_cb(cb):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT * FROM articulo WHERE cb='{cb}'"
            cursor.execute(sql)
            articulo=cursor.fetchone()

            if articulo:
                return 'El artículo existe'
            else:
                return None

    def __str__(self):
        return f"{self.id} - {self.nombre} "
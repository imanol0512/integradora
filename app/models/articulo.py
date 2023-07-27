from .db import get_connection

mydb=get_connection()

class Categoria:
    def __init(self,nombre,id=None):
        self.id=id
        self.nombre=nombre

class Articulo:

    def __init__(self,cb,nombre,precio,marca,categoria,existencias,id=None):
        self.id=id
        self.cb=cb
        self.nombre=nombre
        self.precio=precio
        self.marca=marca
        self.categoria=categoria
        self.existencias=existencias

    def save(self):
        #Creación de nuevo objeto a DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql="INSERT INTO articulo(cb,nombre,precio,marca,categoria,existencias) VALUES (%s,%s,%s,%s,%s,%s)"
                val=(self.cb,self.nombre,self.precio,self.marca,self.categoria,self.existencias)
                cursor.execute(sql,val)
                mydb.commit()
                self.id=cursor.lastrowid
                return self.id
        #Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql="UPDATE articulo SET cb = %s,nombre = %s,precio = %s,marca = %s, categoria = %s, existencias = %s WHERE id = %s"
                val=(self.cb,self.nombre,self.precio,self.marca,self.categoria,self.existencias,self.id)
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
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT articulo.cb,articulo.nombre,articulo.precio,articulo.marca,categoria.nombre,articulo.existencias FROM articulo inner join categoria on categoria.id=articulo.categoria WHERE id={id}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             articulo=Articulo(result["cb"],result["nombre"],result["precio"],result["marca"],result["categoria"],result["existencias"],id)
             return articulo

    #Consulta    
    @staticmethod
    def get_all():
        articulos=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT cb,articulo.nombre,articulo.precio,articulo.marca,categoria.nombre,articulo.existencias FROM articulo inner join categoria on categoria.id=articulo.categoria"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulos.append(Articulo(item["cb"],item["nombre"],item["precio"],item["marca"],item["existencias"],item["id"]),Categoria(item["nombre"],item["id"]))
            return articulos
        
    #Contar
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql=f"SELECT COUNT(id) FROM articulo"
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
                return 'User exist'
            else:
                return None

    def __str__(self):
        return f"{self.id} - {self.nombre} "
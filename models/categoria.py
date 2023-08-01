from .db import get_connection

mydb=get_connection()

class Categoria:
    def __init__(self,nombre,id=None):
        self.id=id
        self.nombre=nombre

    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT id,nombre from categoria where id={id}"
            cursor.execute(sql)
            result=cursor.fetchone()
            print(result)
            categoria=Categoria(result["nombre"],id)
            return categoria

    @staticmethod
    def get_all():
        categorias=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT id,nombre FROM categoria"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                categorias.append(Categoria(item["nombre"],item["id"]))
            return categorias

    def __str__(self):
        return f"{self.id} - {self.nombre} "
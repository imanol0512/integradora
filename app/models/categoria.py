from .db import get_connection

mydb=get_connection()

class Categoria:

    def __init__(self,nombre,id=None):
        self.id=id
        self.nombre=nombre

    def save(self):
        #Creación de nuevo objeto a DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql="INSERT INTO categoria(nombre)"
                val=(self.nombre)
                cursor.execute(sql,val)
                mydb.commit()
                self.id=cursor.lastrowid
                return self.id
        #Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql="UPDATE categoria SET nombre = %s WHERE id = %s"
                val=(self.nombre,self.id)
                cursor.execute(sql,val)
                mydb.commit()
                return self.id
            
    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM categoria WHERE id={self.id}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.id
            
    #Selección
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT nombre FROM categoria WHERE id={id}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             categoria=Categoria(result["nombre"],id)
             return categoria

    #Consulta    
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
        
    #Contar
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql=f"SELECT COUNT(id) FROM categoria"
            cursor.execute(sql)
            result=cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{self.id} - {self.nombre} "
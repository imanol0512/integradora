from .db import get_connection

mydb=get_connection()

class Venta:

    def __init__(self,fecha,id=None):
        self.id=id
        self.fecha=fecha

    def save(self):
        #Creación de nuevo objeto a DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql="INSERT INTO categoria(fecha)"
                val=(self.fecha)
                cursor.execute(sql,val)
                mydb.commit()
                self.id=cursor.lastrowid
                return self.id
        #Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql="UPDATE categoria SET nombre = %s WHERE id = %s"
                val=(self.fecha,self.id)
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
             sql=f"SELECT fecha FROM categoria WHERE id={id}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             fecha=Venta(result["fecha"],id)
             return fecha

    #Consulta    
    @staticmethod
    def get_all():
        ventas=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT id,fecha FROM venta"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                ventas.append(Venta(item["fecha"],item["id"]))
            return ventas
        
    #Contar
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql=f"SELECT COUNT(id) FROM venta"
            cursor.execute(sql)
            result=cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{self.id} - {self.fecha} "
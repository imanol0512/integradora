from .db import get_connection

mydb=get_connection()

class Venta:

    def __init__(self,fecha,id=None):
        self.id=id
        self.fecha=fecha

    def registrar_venta(self):
        #Creación de nuevo objeto a DB con idventa
        with mydb.cursor() as cursor:
             sql="INSERT into venta(id,fecha) VALUES %s, TIMESTAMP()"
             cursor.execute(sql)
             mydb.commit()
             self.id=cursor.lastrowid
             return self.id,self.fecha
            
    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM venta WHERE id={self.id}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.id
            
    #Selección
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT id,fecha FROM venta WHERE id={id}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             venta=Venta(result["fecha"],id)
             return venta

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
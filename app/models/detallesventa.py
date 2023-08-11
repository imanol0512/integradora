from .db import get_connection

mydb=get_connection()

class DetallesVenta:

    def __init__(self,idventa,idarticulo,cantidad):
        self.idventa=idventa
        self.idarticulo=idarticulo
        self.cantidad=cantidad

    def save(self):
    #Creación de artículo temporal
        if self.idarticulo is None:
            with mydb.cursor() as cursor:
                sql="INSERT INTO detallesventa(idarticulo,cantidad)"
                val=(self.idarticulo,self.cantidad)
                cursor.execute(sql,val)
                mydb.commit()
                return self.idarticulo
    # Actualizar artículo temporal
        else:
            with mydb.cursor() as cursor:
                sql="INSERT INTO detallesventa(idarticulo,cantidad)"
                val=(self.idarticulo,self.cantidad)
                cursor.execute(sql,val)
                mydb.commit()
                return self.idventa,self.idarticulo

    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM detallesventa WHERE idventa IS NULL AND idarticulo={self.idarticulo}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.idventa,self.idarticulo

    #Cancelar venta y sus objetos
    def delete_all(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM detallesventa WHERE idventa IS NULL"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.idventa

    #Selección
    @staticmethod
    def get_one(idventa,idarticulo):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT articulo.name as 'idarticulo',cantidad FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa={idventa} and detallesventa.idarticulo={idarticulo}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             articuloVenta=DetallesVenta(result["idarticulo"],result["cantidad"])
             return articuloVenta

    #Consulta    
    @staticmethod
    def get(idventa):
        articulosVenta=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT articulo.name as 'idarticulo',cantidad FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa={idventa}"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulosVenta.append(DetallesVenta(item["idarticulo"],item["cantidad"]))
            return articulosVenta

    #Acciones en nueva venta

    def get_new(idarticulo):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT articulo.name as 'idarticulo',cantidad FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa IS NULL and detallesventa.idarticulo={idarticulo}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             articuloVenta=DetallesVenta(result["idarticulo"],result["cantidad"])
             return articuloVenta

    def get_all_new():
        articulosVenta=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT articulo.name as 'idarticulo',cantidad FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa IS NULL"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulosVenta.append(DetallesVenta(item["idarticulo"],item["cantidad"]))
            return articulosVenta
        
    def delete_new(self):
        with mydb.cursor() as cursor:
            sql=f"DELETE FROM detallesventa WHERE idventa IS NULL and idarticulo={self.idarticulo}"
            cursor.execute(sql)
            mydb.commit()
            return self.idarticulo

    def cancel(self):
        with mydb.cursor() as cursor:
            sql=f"DELETE FROM detallesventa WHERE idventa IS NULL"
            cursor.execute(sql)
            mydb.commit()
            return self.idventa

    #Subtotal (mover como rutina en SQL luego)
    @staticmethod
    def subtotal_consulta(idventa,idarticulo):
        with mydb.cursor() as cursor:
            sql="SELECT (articulo.precio*detallesventa.cantidad) as 'subtotal' from detallesventa inner join articulo on articulo.id=detallesventa.idarticulo where detallesventa.idventa = %s and detallesventa.idarticulo = %s"
            cursor.execute(sql)
            mydb.commit()
            return #TBD

    @staticmethod
    def total_consulta(idventa):
        with mydb.cursor() as cursor:
            sql="SELECT sum(articulo.precio*detallesventa.cantidad) as 'total' from detallesventa inner join articulo on articulo.id=detallesventa.idarticulo"
            cursor.execute(sql)
            mydb.commit()
            return #TBD

    def __str__(self):
        return f"{self.id} - {self.fecha} "
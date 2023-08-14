from .db import get_connection

mydb=get_connection()

class DetallesVenta:

    def __init__(self,idventa,idarticulo,cantidad):
        self.idventa=idventa
        self.idarticulo=idarticulo
        self.cantidad=cantidad

    def save(self):
    #Creación de artículo temporal
            with mydb.cursor() as cursor:
                sql="INSERT INTO detallesventa(idarticulo, cantidad) VALUES (%s, %s)"
                val=(self.idarticulo,self.cantidad)
                cursor.execute(sql,val)
                print(val)
                mydb.commit()
                return self.idarticulo
    # Actualizar artículo temporal        
    def update(self):
        with mydb.cursor() as cursor:
            sql="UPDATE detallesventa SET cantidad=%s WHERE idarticulo=%s AND idventa IS NULL"
            val=(self.cantidad,self.idarticulo)
            cursor.execute(sql,val)
            mydb.commit()
            return self.idarticulo

    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM detallesventa WHERE idventa IS NULL AND idarticulo={self.idarticulo}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.idarticulo

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
             sql=f"SELECT articulo.nombre as 'idarticulo',cantidad FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa={idventa} and detallesventa.idarticulo={idarticulo}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             articuloVenta=DetallesVenta(result["idarticulo"],result["cantidad"])
             return articuloVenta

    #Consulta    
    @staticmethod
    def get(idventa):
        articulosVenta=[]
        subtotales = []
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT idventa,articulo.nombre as 'idarticulo',cantidad,articulo.precio*cantidad as subtotal FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa={idventa}"
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result)
            for item in result:
                subtotales.append(item['subtotal'])
                articulosVenta.append(DetallesVenta(item["idventa"],item["idarticulo"],item["cantidad"]))
            return {'articulosVenta': articulosVenta,
                    'subtotales':subtotales}

    #Acciones en nueva venta

    def get_new(idarticulo):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT articulo.nombre as 'idarticulo',cantidad FROM detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa IS NULL and detallesventa.idarticulo={idarticulo}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             articuloVenta=DetallesVenta('',result["idarticulo"],result["cantidad"])
             return articuloVenta
    
    def get_new_with_id(idarticulo):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT idarticulo,cantidad FROM detallesventa WHERE idventa IS NULL and idarticulo={idarticulo}"
            cursor.execute(sql)
            result=cursor.fetchone()
            print(result)
            articuloVenta=DetallesVenta('',result["idarticulo"],result["cantidad"])
            return articuloVenta

    def get_all_new():
        articulosVenta=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT idventa,articulo.name as 'idarticulo',cantidad FROM detallesventa INNER JOIN articulo ON articulo.id=detallesventa.idarticulo WHERE idventa IS NULL"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulosVenta.append(DetallesVenta(item["idventa"],item["idarticulo"],item["cantidad"]))
            return articulosVenta

    def subtotal_new(idarticulo):
        with mydb.cursor() as cursor:
            sql=f"SELECT existencias*cantidad FROM detallesventa INNER JOIN articulo ON articulo.id=detallesventa.idarticulo WHERE idventa IS NULL and idarticulo={idarticulo}"
            cursor.execute(sql)
            result=cursor.fetchone()
            print(result)
            return result[0]
    
    def total_new():
        with mydb.cursor() as cursor:
            sql="SELECT sum(articulo.precio*detallesventa.cantidad) as total from detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa IS NULL"
            cursor.execute(sql)
            result=cursor.fetchone()
            mydb.commit()
            print(result)
            return result[0]

    def cancel():
        with mydb.cursor() as cursor:
            sql=f"DELETE FROM detallesventa WHERE idventa IS NULL"
            cursor.execute(sql)
            mydb.commit()

    #Subtotal (mover como rutina en SQL luego)
    @staticmethod
    def subtotal_consulta(idventa):
        subtotal=[]
        with mydb.cursor(dictionary=True,buffered=True) as cursor:
            sql=f"SELECT articulo.precio*detallesventa.cantidad as subtotal from detallesventa inner join articulo on articulo.id=detallesventa.idarticulo where detallesventa.idventa = {idventa}"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                subtotal.append(item["subtotal"])
            return subtotal

    @staticmethod
    def total_consulta(idventa):
        with mydb.cursor() as cursor:
            sql=f"SELECT sum(articulo.precio*detallesventa.cantidad) as total from detallesventa inner join articulo on articulo.id=detallesventa.idarticulo WHERE idventa={idventa}"
            cursor.execute(sql)
            result=cursor.fetchone()
            mydb.commit()
            print(result)
            return result[0]

    def __str__(self):
        return f"{self.idventa} - {self.idarticulo} "
    
class VistaDetalles:
    def __init__(self,idventa,nombre,cantidad,subtotal):
        self.idventa=idventa
        self.nombre=nombre
        self.cantidad=cantidad
        self.subtotal=subtotal


    @staticmethod
    def get_new_id(nombre):
        with mydb.cursor(buffered=True) as cursor:
            sql=f"SELECT idarticulo FROM detallesventa INNER JOIN articulo on articulo.id=detallesventa.idarticulo WHERE articulo.nombre='{nombre}'"
            cursor.execute(sql)
            result=cursor.fetchone()
            mydb.commit()
            print(result)
            cursor.close()
            return result[0]

    @staticmethod
    def get_all_new():
        articulosVenta=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT idventa,nombre,cantidad,subtotal FROM crear_venta"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                articulosVenta.append(VistaDetalles(None,item["nombre"],item["cantidad"],item["subtotal"]))
            cursor.close()
            return articulosVenta        

    @staticmethod
    def get_all(idventa):
        articulosVenta = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT idventa, articulo.nombre as nombre, cantidad, cantidad * precio as subtotal FROM detallesventa inner join articulo on articulo.id = detallesventa.idarticulo WHERE idventa = {idventa}"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                articulosVenta.append(item["idventa"])
                articulosVenta.append(item["nombre"])
                articulosVenta.append(item["cantidad"])
                articulosVenta.append(item["subtotal"])
            mydb.commit()
            cursor.close()
        return articulosVenta
from .db import get_connection

mydb=get_connection()

class Proveedor:

    def __init__(self,nombre,apellido,telefono,direccion,numdireccion,colonia,municipio,estado,id=None):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.direccion=direccion
        self.numdireccion=numdireccion
        self.colonia=colonia
        self.municipio=municipio
        self.estado=estado

    def save(self):
        #Creación de nuevo objeto a DB
        if self.id is None:
            with mydb.cursor() as cursor:
                sql="INSERT INTO proveedor(nombre,apellido,telefono,direccion,numdireccion,colonia,municipio,estado) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                val=(self.nombre,self.apellido,self.telefono,self.direccion,self.numdireccion,self.colonia,self.municipio,self.estado)
                cursor.execute(sql,val)
                mydb.commit()
                self.id=cursor.lastrowid
                return self.id
        #Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql="UPDATE proveedor SET nombre = %s,apellido = %s, telefono = %s, direccion = %s, numdireccion = %s, colonia = %s, municipio = %s, estado = %s WHERE id = %s"
                val=(self.nombre,self.id)
                cursor.execute(sql,val)
                mydb.commit()
                return self.id
            
    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM proveedor WHERE id={self.id}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.id
            
    #Selección por ID
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
             sql=f"SELECT nombre FROM proveedor WHERE id={id}"
             cursor.execute(sql)
             result=cursor.fetchone()
             print(result)
             proveedor=Proveedor(result["nombre"],result["apellido"],result["telefono"],result["direccion"],result["numdireccion"],result["colonia"],result["municipio"],result["estado"],id)
             return proveedor

    #Consulta todos los proveedores   
    @staticmethod
    def get_all(limit=15,page=1):
        offset=limit*page-limit
        proveedores=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT id,nombre,apellido,telefono,direccion,numdireccion,colonia,municipio,estado FROM proveedor LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result=cursor.fetchall()
            for item in result:
                proveedores.append(Proveedor(item["nombre"], item["apellido"], item["telefono"], item["direccion"], item["numdireccion"], item["colonia"], item["municipio"], item["estado"], item["id"]))
            return proveedores
        
    #Contar total de proveedores
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql=f"SELECT COUNT(id) FROM proveedor"
            cursor.execute(sql)
            result=cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido}"
from .db import get_connection

mydb = get_connection()

class Proveedor:

    def __init__(self, nombre, apellido, telefono, direccion, numdireccion, colonia, municipio, estado, id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.numdireccion = numdireccion
        self.colonia = colonia
        self.municipio = municipio
        self.estado = estado

    def save(self):
        # Creación de nuevo objeto en la DB
        if self.id is None:
            with mydb.cursor() as cursor:
<<<<<<< HEAD
                sql="INSERT INTO proveedor(nombre,apellido,telefono,direccion,numdireccion,colonia,municipio,estado) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                val=(self.nombre,self.apellido,self.telefono,self.direccion,self.numdireccion,self.colonia,self.municipio,self.estado)
                cursor.execute(sql,val)
=======
                sql = "INSERT INTO proveedor (nombre, apellido, telefono, direccion, numdireccion, colonia, municipio, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.nombre, self.apellido, self.telefono, self.direccion, self.numdireccion, self.colonia, self.municipio, self.estado)
                cursor.execute(sql, val)
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339
                mydb.commit()
                self.id = cursor.lastrowid
                return self.id
        # Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE proveedor SET nombre = %s, apellido = %s, telefono = %s, direccion = %s, numdireccion = %s, colonia = %s, municipio = %s, estado = %s WHERE id = %s"
                val = (self.nombre, self.apellido, self.telefono, self.direccion, self.numdireccion, self.colonia, self.municipio, self.estado, self.id)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id
            
    # Eliminar objeto
    def delete(self):
<<<<<<< HEAD
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM proveedor WHERE id={self.id}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.id
            
    #Selección por ID
=======
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM proveedor WHERE id = {self.id}"
            cursor.execute(sql)
            mydb.commit()
            return self.id
            
    # Selección por ID
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339
    @staticmethod
    def get(id):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM proveedor WHERE id = {id}"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                proveedor = Proveedor(result["nombre"], result["apellido"], result["telefono"], result["direccion"], result["numdireccion"], result["colonia"], result["municipio"], result["estado"], result["id"])
                return proveedor
            return None

<<<<<<< HEAD
    #Consulta todos los proveedores   
    @staticmethod
    def get_all(limit=15,page=1):
        offset=limit*page-limit
        proveedores=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT id,nombre,apellido,telefono,direccion,numdireccion,colonia,municipio,estado FROM proveedor LIMIT { limit } OFFSET { offset }"
=======
    # Consulta todos los proveedores
    @staticmethod
    def get_all():
        proveedores = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM proveedor"
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                proveedores.append(Proveedor(item["nombre"], item["apellido"], item["telefono"], item["direccion"], item["numdireccion"], item["colonia"], item["municipio"], item["estado"], item["id"]))
            return proveedores
        
<<<<<<< HEAD
    #Contar total de proveedores
=======
    # Contar número total de proveedores
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = "SELECT COUNT(id) FROM proveedor"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido}"

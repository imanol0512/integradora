from .db import get_connection
from werkzeug.security import generate_password_hash,check_password_hash

mydb=get_connection()

class Usuario:

    def __init__(self,
                 nombreusuario,
                 contrasena,
                 is_admin,
                 idusuario=None):
        self.idusuario=idusuario
        self.nombreusuario=nombreusuario
        self.contrasena=contrasena
        self.is_admin=is_admin

    def save(self):
        #Creación de nuevo objeto a DB
        if self.idusuario is None:
            with mydb.cursor() as cursor:
                self.contrasena=generate_password_hash(self.contrasena)
                sql="INSERT INTO usuario(nombre,contrasena,is_admin) VALUES (%s,%s,%s)"
                val=(self.nombreusuario,self.contrasena,self.is_admin)
                cursor.execute(sql,val)
                mydb.commit()
                self.idusuario=cursor.lastrowid
                return self.idusuario
        #Actualizar objeto
        else:
            with mydb.cursor() as cursor:
                sql="UPDATE user SET nombreusuario = %s,contrasena=%s,is_admin=%s WHERE idusuario = %s"
                val=(self.nombreusuario,self.contrasena,self.is_admin,self.idusuario)
                cursor.execute(sql,val)
                mydb.commit()
                return self.idusuario
            
    #Eliminar objeto
    def delete(self):
            with mydb.cursor() as cursor:
                 sql=f"DELETE FROM usuario WHERE idusuario={self.idusuario}"
                 cursor.execute(sql)
                 mydb.commit()
                 return self.idusuario
            
    #Selección
    @staticmethod
    def __get__(idusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT * FROM usuarios WHERE idusuario={idusuario}"
            cursor.execute(sql)
            usuario=cursor.fetchone()
            if usuario:
                usuario=Usuario(nombreusuario=usuario["nombreusuario"],
                                contrasena=usuario["contrasena"],
                                is_admin=usuario["is_admin"],
                                idusuario=idusuario)
                return usuario
            
            return None

    #Validar nombre usuario
    def check_username(nombreusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT * FROM usuario WHERE nombreusuario='{nombreusuario}'"
            cursor.execute(sql)
            usuario=cursor.fetchone()

            if usuario:
                return 'User exist'
            else:
                return None

    @staticmethod
    def get_by_password(nombreusuario,contrasena):
        with mydb.cursor(dictionary=True) as cursor:
            sql="SELECT idusuario,nombreusuario,contrasena FROM usuario WHERE nombreusuario = %s"
            val=(nombreusuario,)
            cursor.execute(sql,val)
            usuario=cursor.fetchone()

            if usuario != None:
                if check_password_hash(usuario["contrasena"],contrasena):
                    return Usuario.__get__(usuario["id"])
            return None

    #Consulta    
    @staticmethod
    def get_all(limit=15,page=1):
        offset=limit*page-limit
        usuarios=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT * FROM usuario LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result=cursor.fetchall()
            for usuario in result:
                usuarios.append(
                    Usuario(usuario=usuario["idusuario"],
                                        contrasena=usuario["contrasena"],
                                        is_admin=usuario["is_admin"],
                                        idusuario=usuario["idusuario"])
                )
            return usuarios
        
        
    def __str__(self):
        return f"{self.idusuario} {self.nombreusuario} "
from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

mydb = get_connection()

class Usuario(UserMixin):
    def __init__(self, nombreusuario, contrasena, is_admin, idusuario=None):
        self.idusuario = idusuario
        self.nombreusuario = nombreusuario
        self.contrasena = contrasena
        self.is_admin = is_admin

    def save(self):
        # Creación de nuevo objeto en la base de datos
        if self.idusuario is None:
            with mydb.cursor() as cursor:
                self.contrasena = generate_password_hash(self.contrasena)
                sql = "INSERT INTO usuario(nombreusuario, contrasena, is_admin) VALUES (%s, %s, %s)"
                val = (self.nombreusuario, self.contrasena, self.is_admin)
                cursor.execute(sql, val)
                mydb.commit()
                self.idusuario = cursor.lastrowid
                return self.idusuario
        # Actualizar objeto existente en la base de datos
        else:
            with mydb.cursor() as cursor:
                user = Usuario.get_by_id(self.idusuario)
                if check_password_hash(user.contrasena, self.contrasena):
                    nueva_contra = user.contrasena
                else:
                    nueva_contra = generate_password_hash(self.contrasena)
                sql = "UPDATE usuario SET nombreusuario = %s, contrasena = %s, is_admin = %s WHERE idusuario = %s"
                val = (self.nombreusuario, nueva_contra, self.is_admin, self.idusuario)
                cursor.execute(sql, val)
                mydb.commit()
                return self.idusuario

    def get_id(self):
        return (self.idusuario)

    def delete(self):
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"DELETE FROM usuario where idusuario={self.idusuario}"
            cursor.execute(sql)
            mydb.commit
            return self.idusuario

    @staticmethod
    def get_all(limit=15,page=1):
        offset=limit*page-limit
        usuarios=[]
        with mydb.cursor(dictionary=True) as cursor:
            sql=f"SELECT idusuario,nombreusuario,contrasena,is_admin FROM usuario LIMIT { limit } OFFSET { offset }"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                usuarios.append(Usuario(item["nombreusuario"],item["contrasena"],item["is_admin"],item["idusuario"]))
            return usuarios

    @staticmethod
    def get_by_username(nombreusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM usuario WHERE nombreusuario = %s"
            cursor.execute(sql, (nombreusuario,))
            usuario = cursor.fetchone()
            if usuario:
                usuario = Usuario(
                    nombreusuario=usuario["nombreusuario"],
                    contrasena=usuario["contrasena"],
                    is_admin=usuario["is_admin"],
                    idusuario=usuario["idusuario"]
                )
                return usuario
            return None

    @staticmethod
    def get_by_id(idusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql="SELECT * FROM usuario WHERE idusuario = %s"
            cursor.execute(sql,(idusuario,))
            usuario=cursor.fetchone()
            if usuario:
                usuario=Usuario(
                    nombreusuario=usuario["nombreusuario"],
                    contrasena=usuario["contrasena"],
                    is_admin=usuario["is_admin"],
                    idusuario=usuario["idusuario"]
                )
                return usuario
            return None

    @staticmethod
    def get_by_password(nombreusuario, password):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT idusuario, nombreusuario, contrasena, is_admin FROM usuario WHERE nombreusuario = %s"
            val=(nombreusuario,)
            cursor.execute(sql, val)
            usuario = cursor.fetchone()
        
            if usuario and check_password_hash(usuario["contrasena"], password):
                return Usuario(nombreusuario=usuario["nombreusuario"], contrasena='', is_admin=usuario["is_admin"], idusuario=usuario["idusuario"])
            
        return None

    @staticmethod
    def check_username(nombreusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM usuario WHERE nombreusuario = '{ nombreusuario }'"
            cursor.execute(sql)

            user = cursor.fetchone()

            if user:
                return 'El usuario existe'
            else:
                return None

    # Verificar contraseña para autenticación
    def verify_password(self, contrasena):
        #return check_password_hash(self.contrasena, contrasena)
        if self.contrasena == contrasena: 
            return True
        else:
            return False
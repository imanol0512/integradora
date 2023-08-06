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
                sql = "UPDATE usuario SET nombreusuario = %s, contrasena = %s, is_admin = %s WHERE idusuario = %s"
                val = (self.nombreusuario, self.contrasena, self.is_admin, self.idusuario)
                cursor.execute(sql, val)
                mydb.commit()
                return self.idusuario
            
    # Eliminar objeto de la base de datos
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM usuario WHERE idusuario = {self.idusuario}"
            cursor.execute(sql)
            mydb.commit()
            return self.idusuario
            
    # Selección de objeto de la base de datos por ID
    @staticmethod
    def __get__(idusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM usuario WHERE idusuario = {idusuario}"
            cursor.execute(sql)
            usuario = cursor.fetchone()
            if usuario:
                usuario = Usuario(
                    nombreusuario=usuario["nombreusuario"],
                    contrasena=usuario["contrasena"],
                    is_admin=usuario["is_admin"],
                    idusuario=idusuario
                )
                return usuario
            
            return None

    # Validar existencia de nombre de usuario en la base de datos
    @staticmethod
    def check_username(nombreusuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM usuario WHERE nombreusuario = '{nombreusuario}'"
            cursor.execute(sql)
            usuario = cursor.fetchone()

            if usuario:
                return 'User exist'
            else:
                return None

    # Obtener usuario por nombre de usuario y contraseña (para autenticación)
    @staticmethod
    def get_by_password(nombreusuario, contrasena):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT idusuario, nombreusuario, contrasena FROM usuario WHERE nombreusuario = %s"
            val = (nombreusuario,)
            cursor.execute(sql, val)
            usuario = cursor.fetchone()

            if usuario is not None:
                if check_password_hash(usuario["contrasena"], contrasena):
                    return Usuario.__get__(usuario["idusuario"])
            return None

    # Obtener todos los usuarios de la base de datos
    @staticmethod
    def get_all(limit=15, page=1):
        offset = limit * page - limit
        usuarios = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT * FROM usuario LIMIT {limit} OFFSET {offset}"
            cursor.execute(sql)
            result = cursor.fetchall()
            for usuario in result:
                usuarios.append(
                    Usuario(
                        nombreusuario=usuario["nombreusuario"],
                        contrasena=usuario["contrasena"],
                        is_admin=usuario["is_admin"],
                        idusuario=usuario["idusuario"]
                    )
                )
            return usuarios

    def __str__(self):
        return f"{self.idusuario} {self.nombreusuario} "

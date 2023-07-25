import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Aquí debes proporcionar tu contraseña de la base de datos si tiene una
        database="spvrb"
    )
<<<<<<< HEAD
    return mydb
=======
    return mydb
>>>>>>> 0e2e00fb6b95018a3fc0c239d7b7947d89197339

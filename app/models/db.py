import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Aquí debes proporcionar tu contraseña de la base de datos si tiene una
        database="spvrb"
    )
    return mydb

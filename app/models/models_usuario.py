from flask_login import UserMixin
import sqlite3

db = sqlite3.connect("app/db/contalcred.db" , check_same_thread=False)

class User(UserMixin):
    def __init__(self,pk,id,usuario,senha):
        self.pk = pk
        self.id = id
        self.usuario = usuario
        self.senha = senha
    
    def get_id(self):
        return self.id


def get_all_users():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()
    lista_usuarios = [
        User(
            pk,id, usuario, senha
        )
        for (
            pk,id, usuario, senha
        ) in resultado
    ]
    return lista_usuarios


def get_user(user_id):
    users = get_all_users()
    for u in users:
        if u.id == user_id:
            return u
    return None
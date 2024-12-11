import sqlite3
from BasesDeDatos import Bdd as cn

class ConexionPrecios():
    
    def __init__(self):

        try:
            self.con3 = cn.Conexion().conectarr()
        except Exception as e:
            print(e)
    
    def conexionPrecios(self):
        return self.con3
import sqlite3
from BasesDeDatos import Bdd as cn

class CrearTablaVuelosEncomiendasP():
    
    def __init__(self):

        try:
            self.con = cn.Conexion().conectarr()
            self.crearTablaVuelosP()
        except Exception as e:
            print(e)
    
    def crearTablaVuelosP(self):
        tablaVuelosP = """CREATE TABLE IF NOT EXISTS vuelosEncomiendasParciales
        (id INTEGER,
        destino TEXT,
        tipoAvion TEXT,
        vuelo INTEGER DEFAULT 0,
        encomienda INTEGER DEFAULT 0,
        kilos INTEGER DEFAULT 0,
        id_pasaje INTEGER PRIMARY KEY AUTOINCREMENT)""" 
              
        #Cursor para ejecutar esta consulta
        cursor = self.con.cursor()
        cursor.execute(tablaVuelosP)
        cursor.close()
        self.con.close()
    
import sqlite3

class ConexionBddVuelosP():
    
    def __init__(self):

        try:
            self.con = sqlite3.connect("BasesDeDatos/AeroChinquihueVuelosP.db")
            self.crearTablaVuelosP()
        except Exception as e:
            print(e)
    
    def crearTablaVuelosP(self):
        tablaVuelosP = """CREATE TABLE IF NOT EXISTS vuelosp 
        (id TEXT,
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
    
    def conectarTablaVuelosP(self):
        return self.con
    
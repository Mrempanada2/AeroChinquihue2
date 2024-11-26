import sqlite3

class ConexionBddVuelos():
    
    def __init__(self):

        try:
            self.conn = sqlite3.connect("AeroChinquihueVuelos.db")
            self.crearTablaVuelos()
        except Exception as e:
            print(e)
    
    def crearTablaVuelos(self):
        tablaVuelos = """CREATE TABLE IF NOT EXISTS vuelos 
        (id TEXT,
        destino TEXT,
        tipoAvion TEXT,
        vuelo INTEGER DEFAULT 0,
        encomienda INTEGER DEFAULT 0,
        pagado INTEGER DEFAULT 0,
        id_pasaje INTEGER PRIMARY KEY AUTOINCREMENT)"""  
              
        #Cursor para ejecutar esta consulta
        curs = self.conn.cursor()
        curs.execute(tablaVuelos)
        curs.close()
    
    def conectarrTrs(self):
        return self.conn
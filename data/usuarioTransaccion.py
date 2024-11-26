import sqlite3

class ConexionTrs():
    
    def __init__(self):
        #Crear variable de instancia para conectarse a la base de datos si no existe (crearTablaDatos) y manejar errores
        try:
            self.conn = sqlite3.connect("AeroChinPagos.db")
            self.crearTablaPagos()
        except Exception as e:
            print(e)
    
    def crearTablaPagos(self):
        tablaUsPagos = """CREATE TABLE IF NOT EXISTS pagos 
        (id TEXT,
        usuario TEXT UNIQUE,
        destino TEXT,
        vuelo INTEGER DEFAULT 0,
        encomienda INTEGER DEFAULT 0)"""        
        #Cursor para ejecutar esta consulta
        curs = self.conn.cursor()
        curs.execute(tablaUsPagos)
        curs.close()
    
    def conectarrTrs(self):
        return self.conn
    

        
        
        
        

        
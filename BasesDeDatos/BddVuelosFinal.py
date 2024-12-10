import sqlite3
#Desde aqui importar la clase que calcula el pago y esa clase se conecta a la base de datos de precios
#Esa clase va a modificar el pago y eso, aunque lo hare DESDE una conexion directa desde esa clase mejor
#Ignora esto xd

class ConexionTablaVuelosF():
    
    
    def __init__(self):
        #Crear variable de instancia para conectarse a la base de datos Final si no existe (crearTablaDatos) y manejar errores
        #A esta base de datos tendra acceso el administrador ya que es la base definitiva, no una especie de plantilla!!
        try:
            self.cno = sqlite3.connect("BasesDeDatos/AeroChinquihuePagosFinal.db")
            self.crearTablaVuelosF()
        except Exception as e:
            print(e) 
            
    def crearTablaVuelosF(self):
        tablaVuelosF = """CREATE TABLE IF NOT EXISTS vuelosF(
        id TEXT,
        destino TEXT,
        tipoAvion TEXT,
        vuelo INTEGER DEFAULT 0,
        encomienda INTEGER DEFAULT 0,
        totalPago DEFAULT 0,
        id_Pasaje TEXT)"""
        
        cursor = self.cno.cursor()
        cursor.execute(tablaVuelosF)
        cursor.close()
        
    def ConexionTablaVuelosF(self):
        return self.cno
    
objeto = ConexionTablaVuelosF()
    

        
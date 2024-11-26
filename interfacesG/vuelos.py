from PyQt6 import uic
import BddVuelos as cn
from interfacesG.InfoCuenta import InfoCuenta
from data.usuarioD import usuarioData
from modelo.usuarioTransaccion import UsuarioTransaccion
import sqlite3



class Vuelos:
    def __init__(self, usuarioID):
        self.id = usuarioID
        self.vuelos = uic.loadUi(r"C:\Users\samue\Desktop\Proyecto\interfacesG\vuelos.ui")
        self.db = cn.ConexionBddVuelos().conectarrTrs()
        self.iniciarUI()
        self.vuelos.show()
        
    def iniciarUI(self):   
        self.vuelos.btnConfirmarV.clicked.connect(self.subirDatosVuelo)
       
    def calcularPago():#################################################################
        pass
         
    def subirDatosVuelo(self, id):
        try:
            self.vuelos.lblError.setText("")
            nuevoVuelo = UsuarioTransaccion(id=self.id, Destino=self.vuelos.DestinoV.currentText(),tipoAvion=self.vuelos.TipoAvion.currentText(),Vuelo=1,Encomienda=0,pagado=0)
            
            insertarUsuarioEnBdd = """INSERT INTO vuelos (id, destino, tipoAvion, vuelo, encomienda, pagado) VALUES (?, ?, ?, ?, ?, ?)"""
            values =(nuevoVuelo._id, nuevoVuelo._destino, nuevoVuelo._tipoAvion, nuevoVuelo._vuelo, nuevoVuelo._encomienda, nuevoVuelo._pagado)
            with self.db:
                self.db.execute(insertarUsuarioEnBdd, values)
                print(f"Usuario insertado id:{self.id}")
                self.vuelos.close()
        except Exception as e:
            print(e)
        
        
        
        #clase coso para realizar el pago, que calcula descuentos del 0 al 100 (cliente frecuente y estado emergencia extremo)
        #ademas pago se conecta con la base de datos de vuelos (tabla) y calcula si estan disponibles o no, por condiciones climaticas
        #o por asientos
        #La tabla de vuelos tiene destinos,tipo avion, vuelo, encomienda, pagado (esas 5 columnas),
        
        #Con otra clase podria calcular el precio y ponerlo al final de la tabla de vuelos como "pagado"
        
        
        #La tabla de vuelos es 1 y recibe entonces destino, tipo de avion, si es vuelo o encomienda (con 1s y 0s) y el precio pagado 4 columnas
        
        
        #El precio pagado, la clase que lo calcula contiene metodos para verificar si hay disponibilidad y el resto de eventos
        
        #Tambien guardar id del usuario xd
        #admin tendra un boton especial para ver usuarios y vuelos, en la mainaerochinquiehue
        
        
        pass
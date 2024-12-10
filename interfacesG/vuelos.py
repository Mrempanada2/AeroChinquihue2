from PyQt6 import uic
from BasesDeDatos import BddVuelos as cn
from data.usuarioTransaccion import usuarioDataT
from modelo.usuarioTransaccion import UsuarioTransaccion
from eventos.precio import CalcularPrecios
import sqlite3

class Vuelos():
    def __init__(self, usuarioID):
        self._id = usuarioID
        self.vuelos = uic.loadUi("interfacesG/vuelos.ui")
        self.mostrarInfoVuelos = uic.loadUi("InterfacesG/InfoAviones.ui")
        self.db = cn.ConexionBddVuelosP().conectarTablaVuelosP()
        self.conn = sqlite3.connect("BasesDeDatos/HorariosVuelos.db")
        self.iniciarUI()
        self.vuelos.show()
        
    def iniciarUI(self):   
        self.vuelos.lblError.setText("")
        self.llenarComboBoxHorarios() 
        self.vuelos.btnInfoAviones.clicked.connect(self.mostrarInfoVuelos.show())
        self.vuelos.btnConfirmarV.clicked.connect(self.procesarOperacion)
        
        
        
    def llenarComboBoxHorarios(self):
        try:
            self.vuelos.seleccionarHora.clear()
            cursor = self.conn.cursor()
            tipoAvion = CalcularPrecios(self._id,1,0).devolverTipoAvion()
            print(f"\nel tipo de avion es {tipoAvion}")
            
            getID = cursor.execute("""SELECT [07:00-09:30], [10:00-12:30], [13:00-15:30], [16:00-18:30], [19:00-21:30], [22:00-01:30] FROM horariosV WHERE TAvion = ? AND ([07:00-09:30] IS NULL OR [10:00-12:30] IS NULL OR [13:00-15:30] IS NULL OR [16:00-18:30] IS NULL OR [19:00-21:30] IS NULL OR [22:00-01:30] IS NULL);""",(tipoAvion,))
            
            resultados = getID.fetchall()
            if resultados:
                for fila in resultados:
                    horarios = ['07:00-09:30', '10:00-12:30', '13:00-15:30', '16:00-18:30', '19:00-21:30', '22:00-01:30']
                    for i, horario in enumerate(fila):
                        if horario is None:
                            self.vuelos.seleccionarHora.addItem(horarios[i])
            else:
                print("No se encontraron horarios libres")
                self.vuelos.lblError.setText("No se encontraron horarios")
                           
        except Exception as e:
            print(f"Error al conectarse a la base de datos {e}")
             
       
       
    def procesarOperacion(self):
        if self.subirDatosVuelo():
            self.calcularPago()
            self.cerrarConexiones()##########################################################################
        else:
            print("Algo fallo al subir los datos parciales y enviarlos a la evaluacion de pago")
    
       
    def calcularPago(self):
        try:
            self.curs  = self.db.cursor()
            obtenerID = self.curs.execute("""SELECT * FROM vuelosp WHERE id = ? """, (self._id,))
            FilaUsTransaccion = obtenerID.fetchone()
        
            if FilaUsTransaccion:
                Pago = CalcularPrecios(FilaUsTransaccion[0],FilaUsTransaccion[3],0)
            
                print (f"Id del usuario es {FilaUsTransaccion[0]}")
                print(f"El Avion es {FilaUsTransaccion[2]}")
                print(f"El Destino es {FilaUsTransaccion[1]}")
                if FilaUsTransaccion[3] == 1:
                    print("Es un vuelo de pasajeros no encomienda")
                else:
                    print("Es una encomienda.")
                print (f"IdVuelo es {FilaUsTransaccion[6]}")
            
            ################### Mas adelante cambiaremos esto para que la conexion se cierre solamente cuando se inserta el vuelo en la tabla de vuelos real
            ############ Haremos que la base de datos de la tabla retorne algo cuando se inserte un usuario correctamente y otra cosa cuando no.
            else:
                return None
            
        except Exception as e:
            print (f"Error al seleccionar de la tabla parcial{e}")
            #self.cerrarConexiones()
            return None

         
    def subirDatosVuelo(self):#A data parcial
        try:
            self.vuelos.lblError.setText("")
            nuevoVuelo = UsuarioTransaccion(id=self._id, Destino=self.vuelos.DestinoV.currentText(),tipoAvion=self.vuelos.TipoAvion.currentText(),Vuelo=1,Encomienda=0, kilos=0)
            self.UsurTr = usuarioDataT(nuevoVuelo)


            insertarUsuarioEnBdd = """INSERT INTO vuelosp (id, destino, tipoAvion, vuelo, encomienda, kilos) VALUES (?, ?, ?, ?, ?, ?)"""
            values =(nuevoVuelo._id, nuevoVuelo._destino, nuevoVuelo._tipoAvion, nuevoVuelo._vuelo, nuevoVuelo._encomienda, nuevoVuelo._kilos)
            with self.db:
                self.db.execute(insertarUsuarioEnBdd, values)
                print(f"Usuario insertado id: {nuevoVuelo._id}")

                return True
        except Exception as e:
            print(f"No se logro insertar los valores en la tabla parcial {e}")
            return False
        
    def cerrarConexiones(self):
        self.db.commit()
        self.conn.commit()
        self.conn.close()
        self.db.close()
        

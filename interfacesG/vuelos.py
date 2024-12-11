from PyQt6 import uic
from BasesDeDatos import Bdd as cn
from data.usuarioTransaccion import usuarioDataT
from modelo.usuarioTransaccion import UsuarioTransaccion

class Vuelos():
    def __init__(self, usuarioID):
        self._id = usuarioID
        self.vuelos = uic.loadUi("interfacesG/vuelos.ui")
        self.iniciarUI()
        self.vuelos.show()
        
    def iniciarUI(self):   
        ###Funcion que llena la combo box
        self.vuelos.btnInfoAviones.clicked.connect(self.abrirInfo)
        self.vuelos.btnConfirmarV.clicked.connect(self.procesarOperacion)##########Boton de aceptar, no de confirmar
        
    def abrirInfo(self):        
        self.infoAviones = uic.loadUi("interfacesG/InfoAviones.ui")
        self.infoAviones.show()                     
        
    def procesarOperacion(self):        
        if self.subirDatosVuelo():
            self.abrirVentanaHorarios()
        #self.calcularPago()
        #self.cerrarConexiones()##########################################################################Cerrar cuando se haya hayado un espacio libre (e insertado el vuelo)

    def calcularPago(self):
        try:
            print("")
            pass
        except Exception as e:
            pass
        finally:
            pass
        
    def abrirVentanaHorarios(self):
        db = cn.Conexion().conectarr()
        self.VentanaHorarios = uic.loadUi("interfacesG/horasDisponibles.ui")
        self.VentanaHorarios.show()
        self.VentanaHorarios.cbHorarios.clear()
        self.VentanaHorarios.No_horarios.setText("")
        
        consulta = """SELECT [07:00-09:30], [10:00-12:30], [13:00-15:30], [16:00-18:30], [19:00-21:30], [22:00-01:30] FROM horariosVuelos WHERE TAvion = ? AND ([07:00-09:30] IS NULL OR [10:00-12:30] IS NULL OR [13:00-15:30] IS NULL OR [16:00-18:30] IS NULL OR [19:00-21:30] IS NULL OR [22:00-01:30] IS NULL)"""
        TipoAvion = (self.UsurTr[2])
        if TipoAvion:
            with db:
                resultados = db.execute(consulta,(TipoAvion,))
                Espacios_libres = resultados.fetchall() 
                if Espacios_libres:
                    for fila in Espacios_libres:
                        horarios = ['07:00-09:30', '10:00-12:30', '13:00-15:30', '16:00-18:30', '19:00-21:30', '22:00-01:30']
                        for i, horario in enumerate(fila):
                            if horario is None:
                                self.VentanaHorarios.cbHorarios.addItem(horarios[i])
                                self.VentanaHorarios.No_horarios.setText("")
                else:
                    self.VentanaHorarios.No_horarios.setText("No hay horarios disponibles")
        else:
            print("Algo salio mal, abrir ventanaHorarios...")
            
        ##Enviar a calcular pagos lo siguiente.(el horario)
        self.VentanaHorarios.cbHorarios.currentText()
        ##Esta otra funcion inserta algo en ese espacio puede ser una id de vuelo  SOLO si se confirma el pago.
        
        
         
    def subirDatosVuelo(self):#A data parcial
        db = cn.Conexion().conectarr()
        try:
            
            nuevoVuelo = UsuarioTransaccion(id=self._id, Destino=self.vuelos.DestinoV.currentText(),tipoAvion=self.vuelos.TipoAvion.currentText(),Vuelo=1,Encomienda=0, kilos=0)
            
            #Formatear los valores para que lleguen bien
            id_int = int(nuevoVuelo._id) 
            destino_str = str(nuevoVuelo._destino)
            tipoAvion_str = str(nuevoVuelo._tipoAvion)
            vuelo_int = int(nuevoVuelo._vuelo)
            encomienda_int = int(nuevoVuelo._encomienda)
            kilos_int = int(nuevoVuelo._kilos)  

            #Se prepara para insertar valores, se crea la consulta y los valores a insertar
            insertarUsuarioEnBdd = """INSERT INTO vuelosEncomiendasParciales (id, destino, tipoAvion, vuelo, encomienda, kilos) VALUES (?, ?, ?, ?, ?, ?)"""
            values =(id_int, destino_str, tipoAvion_str, vuelo_int, encomienda_int, kilos_int)

    
            #Se insertan en la tabla parcial, y se extraen sus valores como una tupla para guardarlos en self.UsurTr
            with db:
                db.execute(insertarUsuarioEnBdd, values)
                print(f"\nUsuario insertado para Vuelo, id es: {nuevoVuelo._id}") 
                               
            self.UsurTr = usuarioDataT(id_int).devolverDatos() 
            with db:
                if self.UsurTr:   
                    print(self.UsurTr)           
                    print(f"Confirmar id del usuario es {self.UsurTr[0]}")
                    print(f"La ID del vuelo es de: {self.UsurTr[6]}")
                    print(f"El tipo de avion es un {self.UsurTr[2]}")
                
                    db.execute("DELETE FROM vuelosEncomiendasParciales WHERE id = ?", (self._id,))
                    print("\nDatos extraidos de la base de datos parcial y borrados exitosamente.")
                
                    return True
                else:
                    return False
        except Exception as e:
            print(f"No se logro insertar los valores en la tabla parcial {e}")
            #db.close()
            return False
        

        

from PyQt6 import uic
from BasesDeDatos import Bdd as cn
from data.usuarioTransaccion import usuarioDataT
from modelo.usuarioTransaccion import UsuarioTransaccion
from eventos.precio import CalcularPrecios



class Encomiendas():
    def __init__(self, usuarioID):
        self.esta_id = usuarioID
        self.encomiendas = uic.loadUi("interfacesG/Encomiendas.ui")
        #self.db = cn.ConexionBddVuelosP().conectarTablaVuelosP()
        self.iniciarUI()
        self.encomiendas.lblError.setText("")
        self.encomiendas.show()
        
    def iniciarUI(self):
        self.encomiendas.btnConfirmarE.clicked.connect(self.procesarOperacion)####Boton de aceptar com tal...
        self.encomiendas.btnInfoAviones.clicked.connect(self.abrirInfo)
        
    def abrirInfo(self):
        self.infoAviones = uic.loadUi("interfacesG/InfoAviones.ui")
        self.infoAviones.show()
        

    def procesarOperacion(self):
        if self.subirDatosEncomienda():
            self.abrirVentanaEncomiendas()

    
    def abrirVentanaEncomiendas(self):
        db = cn.Conexion().conectarr()
        self.VentanaEncomiendas = uic.loadUi("interfacesG/PesosDisponiblesHoras.ui")
        self.VentanaEncomiendas.show()
        self.VentanaEncomiendas.cbEncomiendasHorarios.clear()
        self.VentanaEncomiendas.NoespacioCarga.setText("")
        
        consulta = """SELECT [07:00-09:30], [10:00-12:30], [13:00-15:30], [16:00-18:30], [19:00-21:30], [22:00-01:30] FROM encomiendas WHERE TAvion = ? 
        AND([07:00-09:30] > ? OR [10:00-12:30] > ? OR [13:00-15:30] > ? OR [16:00-18:30] > ? OR [19:00-21:30] > ? OR [22:00-01:30] > ?)"""
        
        try:
            kilos = self.kilos
            self.encomiendas.lblError.setText("")
        except ValueError as e:
            self.encomiendas.lblError.setText("Ingrese un valor numerico")
            
        TipoAvion = (self.UsurEn[2])
        if TipoAvion:
            with db:
                resultados = db.execute(consulta, (TipoAvion, kilos, kilos, kilos, kilos, kilos, kilos))
                CapacidadLibre = resultados.fetchall() 
                if CapacidadLibre:
                    for fila in CapacidadLibre:
                        horarios = ['07:00-09:30', '10:00-12:30', '13:00-15:30', '16:00-18:30', '19:00-21:30', '22:00-01:30']
                        for i, horario in enumerate(fila):
                            if horario is not None and horario > kilos:
                                self.VentanaEncomiendas.cbEncomiendasHorarios.addItem(horarios[i])
                                self.VentanaEncomiendas.NoespacioCarga.setText("")
                else:
                    self.VentanaEncomiendas.NoespacioCarga.setText("")
        
        
    def subirDatosEncomienda(self):
        db = cn.Conexion().conectarr()
        
        try:
            
            with db:
                if int(self.encomiendas.EPeso.text())<=45 and int(self.encomiendas.EPeso.text())>=1:
                    self.kilos = int(self.encomiendas.EPeso.text())
                    self.encomiendas.lblError.setText("")
                
                elif int(self.encomiendas.EPeso.text())>45 or int(self.encomiendas.EPeso.text())<1:
                    self.kilos = 0
                    self.encomiendas.lblError.setText("Ingrese un valor valido (maximo 45 kilos)")
                    self.encomiendas.EPeso.setFocus()
                
                else:
                    self.kilos = 0
                    self.encomiendas.lblError.setText("Ingrese un valor valido")
                    self.encomiendas.EPeso.setFocus()
                
            
            nuevaEncomienda = UsuarioTransaccion(id=self.esta_id, Destino=self.encomiendas.Edestino.currentText(),tipoAvion=self.encomiendas.EAvion.currentText(),Vuelo=0,Encomienda=1, kilos=self.kilos)
            
            
            id_int = int(nuevaEncomienda._id) 
            destino_str = str(nuevaEncomienda._destino)
            tipoAvion_str = str(nuevaEncomienda._tipoAvion)
            vuelo_int = int(nuevaEncomienda._vuelo)
            encomienda_int = int(nuevaEncomienda._encomienda)
            kilos_int = int(nuevaEncomienda._kilos) 


            insertarUsuarioEnBdd = """INSERT INTO vuelosEncomiendasParciales (id, destino, tipoAvion, vuelo, encomienda, kilos) VALUES (?, ?, ?, ?, ?, ?)"""
            print("Completado 50%")
            values =(id_int, destino_str, tipoAvion_str, vuelo_int, encomienda_int, kilos_int)
            
            with db:
                db.execute(insertarUsuarioEnBdd, values)
                print(f"\nTransaccion Encomienda parcial insertada. id: {id_int}")
                print("completado 60%")
                
            self.UsurEn = usuarioDataT(id_int).devolverDatos()
            print("completado 70%")
            borrar_lineas = """DELETE FROM vuelosEncomiendasParciales WHERE id = ?"""
            
            if self.UsurEn and self.UsurEn[0] is not None:
                IdABorrar = int(self.UsurEn[0])
            else:
                print("Error: No se encontró un ID válido en self.UsurEn")

            print("completado 80%")
            with db:
                if self.UsurEn:
                    print(self.UsurEn)           
                    print(f"Confirmar id del usuario es {self.UsurEn[0]}")
                    print(f"La ID del vuelo es de: {self.UsurEn[6]}")
                    print(f"El tipo de avion es un {self.UsurEn[2]}")
                    print(f"Los kilos son de {self.UsurEn[5]}")
                    print("completado 85%")
                    db.execute(borrar_lineas,(IdABorrar,))
                    print("completado 90%")
                    print("\nDatos extraidos de la base de datos parcial y borrados exitosamente.")
                    return True
                else:
                    return False           
        except Exception as e:
            print(f"No se logro insertar los valores en la tabla parcial {e}")
            return False
        
        
        


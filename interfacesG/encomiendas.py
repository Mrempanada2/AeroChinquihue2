from PyQt6 import uic
from BasesDeDatos import BddVuelos as cn
from interfacesG.InfoCuenta import InfoCuenta
from data.usuarioTransaccion import usuarioDataT
from modelo.usuarioTransaccion import UsuarioTransaccion
from eventos.precio import CalcularPrecios



class Encomiendas():
    def __init__(self, usuarioID):
        self._id = usuarioID
        self.encomiendas = uic.loadUi("interfacesG/Encomiendas.ui")
        self.mostrarInfoVuelos = uic.loadUi("InterfacesG/InfoAviones.ui")
        self.db = cn.ConexionBddVuelosP().conectarTablaVuelosP()
        self.iniciarUI()
        self.encomiendas.lblError.setText("")
        self.encomiendas.show()
        
    def iniciarUI(self):
        self.encomiendas.btnConfirmarE.clicked.connect(self.procesarOperacion)
        self.encomiendas.btnInfoAviones.clicked.connect(self.mostrarInfoVuelos.show())
        

    def procesarOperacion(self):
        if self.subirDatosEncomienda():
            self.calcularPago()
            self.cerrarConexiones()

    
    def calcularPago(self):
        self.curs = self.db.cursor()
        obtenerID = self.curs.execute("SELECT * FROM vuelosp WHERE id = ? ", (self._id,))
        filaUsTransaccion = obtenerID.fetchone()
        
        if filaUsTransaccion:
            Pago = CalcularPrecios(filaUsTransaccion[0],0,filaUsTransaccion[4])
            
            print (f"Id del usuario es {filaUsTransaccion[0]}")
            print(f"El Avion es {filaUsTransaccion[2]}")
            print(f"El Destino es {filaUsTransaccion[1]}")
            if filaUsTransaccion[4] == 1:
                print("Es una encomienda")
            else:
                print("Es un vuelo de pasajeros")
            print (f"IdVuelo es {filaUsTransaccion[6]}")
    
    def subirDatosEncomienda(self):#A base de datos parcial
        try:
            
            if int(self.encomiendas.EPeso.text())<=20 and int(self.encomiendas.EPeso.text())>=1:
                self.kilos = int(self.encomiendas.EPeso.text())
                self.encomiendas.lblError.setText("")
            elif int(self.encomiendas.EPeso.text())>=20 or int(self.encomiendas.EPeso.text())<=1:
                self.encomiendas.lblError.setText("Ingrese un valor valido (maximo 20 kilos)")
                self.encomiendas.EPeso.setFocus()
            else:
                self.encomiendas.lblError.setText("Ingrese un valor valido")
                self.encomiendas.EPeso.setFocus()
                
            
            nuevaEncomienda = UsuarioTransaccion(id=self._id, Destino=self.encomiendas.Edestino.currentText(),tipoAvion=self.encomiendas.EAvion.currentText(),Vuelo=0,Encomienda=1, kilos=self.kilos)
            self.UsurTr = usuarioDataT(nuevaEncomienda)


            insertarUsuarioEnBdd = """INSERT INTO vuelosp (id, destino, tipoAvion, vuelo, encomienda, kilos) VALUES (?, ?, ?, ?, ?, ?)"""
            values =(nuevaEncomienda._id, nuevaEncomienda._destino, nuevaEncomienda._tipoAvion, nuevaEncomienda._vuelo, nuevaEncomienda._encomienda, nuevaEncomienda._kilos)
            with self.db:
                self.db.execute(insertarUsuarioEnBdd, values)
                print(f"Transaccion parcial insertada. id: {nuevaEncomienda._id}")
                return True
        except Exception as e:
            print(f"No se logro insertar los valores en la tabla parcial {e}")
            return False
        
    def cerrarConexiones(self):
        self.db.commit()
        self.encomiendas.close()
        self.db.close()
        
        


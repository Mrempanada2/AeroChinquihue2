from PyQt6 import uic
from interfacesG.InfoCuenta import InfoCuenta
from interfacesG.vuelos import Vuelos
from interfacesG.encomiendas import Encomiendas
from BasesDeDatos.BddVuelos import CrearTablaVuelosEncomiendasP
from BasesDeDatos.BddVuelosFinal import CrearTablaVuelosEncomiendasF

class AeroChinquihuePrincipal():
    def __init__(self, usuarioID):
        #Guardar el ID del usuario que haya ingresado
        self.usuarioID1 = usuarioID 
        
        #Inicializar tabla de Vuelos y encomiendas Parciales, Final y la de Precios en la base de datos
        TablaVuelosP = CrearTablaVuelosEncomiendasP()
        TablaVuelosF = CrearTablaVuelosEncomiendasF()
        #TablaPrecios = ConexionPrecios()
        
        #Probar id que este bien transferida print(self.usuarioID1)
        self.aeroChPrin = uic.loadUi("interfacesG/AeroChinMain.ui")
        self.iniciarUI()
        self.aeroChPrin.show()

    def iniciarUI(self):
        self.aeroChPrin.btnVerMiCuenta.triggered.connect(self.abrirInfo)#
        self.aeroChPrin.btnVuelos.clicked.connect(self.abrirVuelos)
        self.aeroChPrin.btnEncomiendas.clicked.connect(self.abrirEncomiendas)

    def abrirInfo(self):
        self.info = InfoCuenta(self.usuarioID1)
    
    def abrirVuelos(self):
        self.vuelos = Vuelos(self.usuarioID1)
        
    def abrirEncomiendas(self):
        self.encomiendas = Encomiendas(self.usuarioID1)


        
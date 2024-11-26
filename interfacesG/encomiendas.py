from PyQt6 import uic


class Encomiendas:
    def __init__(self,usuarioID):
        usuarioID1 = usuarioID
        self.encomiendas = uic.loadUi(r"C:\Users\samue\Desktop\Proyecto\interfacesG\Encomiendas.ui")
        #self.iniciarUI()
        self.encomiendas.show()
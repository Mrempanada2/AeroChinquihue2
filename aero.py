from PyQt6.QtWidgets import QApplication

from interfacesG.login import Login

class Aero():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        #Ejecutar la aplicacion
        self.app.exec()
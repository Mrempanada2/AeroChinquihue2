from PyQt6 import uic
import sqlite3


class InfoCuenta:
    def __init__(self,usuarioID):
        #Cargar interfaz grafica con uic.loadUI
        self.estaID = usuarioID
        self.inf = uic.loadUi("interfacesG/InfoCuenta.ui")
        self.iniciarUI(usuarioID)
        self.inf.show()
        
    def iniciarUI(self, usuarioID):
        infoUsuario = self.obtenerInfo(usuarioID)
        if infoUsuario:
            self.inf.txtNombre.setText(infoUsuario[0])
            self.inf.txtUsuario.setText(infoUsuario[1])
            self.inf.txtContrasena.setText(infoUsuario[2])
            self.inf.txtNumeroV.setText(str(infoUsuario[3]))
            self.inf.txtID.setText(str(self.estaID))
            if infoUsuario[4] == 1:
                self.inf.txtPersonalE.setText("Es personal de emergencias")
            else:
                self.inf.txtPersonalE.setText("No es personal de emergencias")
            if infoUsuario[5] == 1:
                self.inf.txtEsAdmin.setText("Eres Administrador")
            else:
                self.inf.txtEsAdmin.setText("")
        else:
            self.inf.txtNombre.setText("???")
            
    def obtenerInfo(self,usuarioId):
        try:
            self.conexion = sqlite3.connect(r"C:\Users\samue\Desktop\Proyecto\AeroChin.db")
            self.cursor = self.conexion.cursor()
            
            #Hacer consulta SQL para obtener la info del usuario
            self.cursor.execute("""SELECT nombre, usuario, contrasena, cantVuelos, pEmergencia, administrador FROM usuarios WHERE id = ?""", (usuarioId,))
            
            Usu_Info = self.cursor.fetchone()
            if Usu_Info:
                return Usu_Info
            else:
                print("No se encontro informacion para esa ID")
                return None
        except Exception as e:
            print("Error al obtener info, error B", e)
            return None

            
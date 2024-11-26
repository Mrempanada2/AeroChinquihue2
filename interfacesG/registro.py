from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from modelo.usuario import Usuario
from Bdd import Conexion
import sqlite3



class Registro:
    def __init__(self):
        self.db = Conexion().conectarr()
        self.valorPemerngencia = 0
        self.registro = uic.loadUi(r"C:\Users\samue\Desktop\Proyecto\interfacesG\Registro.ui")
        self.iniciarUI()
        self.registro.lblError.setText("")
        self.registro.show()
             
    def registrarse(self):
        if len(self.registro.txtNombreR.text()) < 1:
            self.registro.lblError.setText("Nombre demasiado corto")
            self.registro.txtNombreR.setFocus()
            
        elif len(self.registro.txtUsuarioR.text()) < 3:
            self.registro.lblError.setText("Nombre del usuario demasiado corto")
            self.registro.txtUsuarioR.setFocus()
            
        elif len(self.registro.txtContrasenaR.text()) < 3:
            self.registro.lblError.setText("Contraseña demasiado corta")
            self.registro.txtContrasenaR.setFocus()
            
        elif (self.registro.txtContrasenaR.text()) != (self.registro.txtContrasenaR2.text()):
            self.registro.lblError.setText("Contraseñas no son iguales")
            self.registro.txtContrasenaR.setFocus()
        else:
            try:
                self.registro.lblError.setText("")                                                                                                                #Insertar si es p emergencia o no según el boton, según una funcion. 
                NuevoUsu = Usuario(nombre=self.registro.txtNombreR.text(),usuario=self.registro.txtUsuarioR.text(), contrasena=self.registro.txtContrasenaR.text(), pEmergencia=self.valorPemerngencia)
                insertarUsuarioEnBdd = """INSERT INTO usuarios (nombre, usuario, contrasena, pEmergencia) VALUES (?, ?, ?, ?)"""
                values =(NuevoUsu._nombre, NuevoUsu._usuario, NuevoUsu._contrasena, NuevoUsu._pEmergencia)
                
                cursor = self.db.cursor()
                cursor.execute(insertarUsuarioEnBdd, values)
                NuevoUsu._id = cursor.lastrowid
                
                self.db.commit()
                cursor.close()
                self.registro.close()
                print(f"Usuario insertado id:{NuevoUsu._id}")


            except sqlite3.IntegrityError as e:
                print("El usuario ya existe o error de datos", e)
                mdBox = QMessageBox()
                mdBox.setWindowTitle("Error")
                mdBox.setIcon(QMessageBox.Icon.Warning)
                mdBox.setText("El usuario ya existe")
                mdBox.exec()
            except Exception as e:
                print("Error al agregar el usuario", e)
                mdBox = QMessageBox()
                mdBox.setWindowTitle("Error")
                mdBox.setIcon(QMessageBox.Icon.Critical)
                mdBox.setText("Error al agregar usuario")
                mdBox.exec()
            
    
    def iniciarUI(self):
        #Aqui se inicializazn y manejan los elementos de la UI
        #Campos a rellenar y botones y checkboxes
        self.registro.btnRegistrarse.clicked.connect(self.registrarse)
        self.registro.btnPeEmergencia.clicked.connect(self.setPeEmergencia)       
            
    def setPeEmergencia(self):
        self.valorPemerngencia = 1 if self.registro.btnPeEmergencia.isChecked() else 0
        #Esto es para comprobar en la consola surante el proceso de desarrollo
        print(f"Estado de Personal de Emergencias: {'Activado' if self.valorPemerngencia else 'Desactivado'}")

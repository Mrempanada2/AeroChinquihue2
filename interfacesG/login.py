from PyQt6 import uic
from modelo.usuario import Usuario
from data.usuarioD import usuarioData
from interfacesG.AeroChinMain import AeroChinquihuePrincipal
from interfacesG.registro import Registro
#En el login se pasa la ID al resto de ventanas, de acuerdo al usuario y contraseña.
class Login():
    def __init__(self):
        self.login = uic.loadUi("interfacesG/login.ui")
        self.iniciarUI()
        self.login.lblError.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblError.setText("Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtContrasena.text()) < 3:
            self.login.lblError.setText("Ingrese una contraseña válida")
            self.login.txtContrasena.setFocus()
        else:
            self.login.lblError.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(), contrasena=self.login.txtContrasena.text())
            Usur = usuarioData()
            user_data = Usur.login(usu)
            if user_data:
                self.main = AeroChinquihuePrincipal(user_data._id)  # Pasar ID del usuario
                self.login.hide()
            else:
                self.login.lblError.setText("Incorrecto, no se encontró\nel usuario")
                
    def openRegistro(self):
        self.registro = Registro()

    def iniciarUI(self):
        self.login.btnIngresar.clicked.connect(self.ingresar)
        self.login.btnRegistrarse.clicked.connect(self.openRegistro)
        


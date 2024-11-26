class Usuario():
    def __init__(self,id=None, nombre="", usuario="", contrasena="", pEmergencia=0, cantVuelos=0, administrador=0):
        #atributos "privados", usar "_"
        self._id = id
        self._nombre = nombre
        self._usuario = usuario
        self._contrasena = contrasena
        self._pEmergencia = pEmergencia
        self._cantVuelos = cantVuelos
        self._administrador = administrador
        
        #REVISAR ID:
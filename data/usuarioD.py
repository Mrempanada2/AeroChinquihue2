import Bdd as cno1
from modelo.usuario import Usuario

class usuarioData():
    
    #Usar los : para que se sepa desde antes que el argumento a recibir es de clase Usuario
    def login(self, usuario:Usuario):
        
        #Funcion para ejecutar consultas
        #Devolver referencia a la base de datos
        self.db = cno1.Conexion().conectarr()
        
        #Cursor para hacer acciones sobre la base de datos.
        self.cursor = self.db.cursor()
        
        resultao = self.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?",(usuario._usuario,usuario._contrasena))
        #Si no existe el usuario
        fila_us = resultao.fetchone()
        if fila_us:
            #Comprobar id print (fila_us[0])
            usuarioT = Usuario(id=fila_us[0],nombre=fila_us[1],usuario=fila_us[2])
            self.cursor.close()
            self.db.close()
            return usuarioT
        else:
            self.cursor.close()
            self.db.close()
            return None
            
        
    
    
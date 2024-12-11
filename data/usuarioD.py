from BasesDeDatos import Bdd as cno1
from modelo.usuario import Usuario


#Esta clase sirve para hayar usuarios que existan en la tabla usuarios
class usuarioData():
    
    #Usar los : para que se sepa desde antes que el argumento a recibir es de clase Usuario
    def login(self, usuario:Usuario):
        
        self.db = cno1.Conexion().conectarr()
        self.cursor = self.db.cursor()      
        resultao = self.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?",(usuario._usuario,usuario._contrasena))

        
        fila_us = resultao.fetchone()
        
        if fila_us:
            usuarioT = Usuario(id=fila_us[0])
            self.cursor.close()
            self.db.close()
            return usuarioT
        else:
            self.cursor.close()
            self.db.close()
            return None
            
        
    
    
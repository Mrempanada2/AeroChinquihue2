from modelo.usuarioTransaccion import UsuarioTransaccion
from BasesDeDatos import BddVuelos as cno2

class usuarioDataT():
    
    def __init__(self, usuarioT:UsuarioTransaccion):
        #Reutilizar conexion de BddVuelos para la abse de AeroChinVuelos
        self.usuarioT = usuarioT
        self.db = cno2.ConexionBddVuelosP().conectarTablaVuelosP()
        #Crear cursor para interactuar con la base de datos
        self.cursor = self.db.cursor()
        self.devolverDatos()
            
        
    def devolverDatos(self):
        resultao = self.cursor.execute("SELECT * FROM vuelosp WHERE id = ?", (str(self.usuarioT._id),))
        Fila_Tr = resultao.fetchone()
        
        if Fila_Tr:
            IdTransaccionParcial = UsuarioTransaccion(id=Fila_Tr[0], Destino=Fila_Tr[1], tipoAvion=Fila_Tr[2], Vuelo=Fila_Tr[3], Encomienda=Fila_Tr[4], kilos=Fila_Tr[5], id_pasaje =Fila_Tr[6])##Modificar esto segun lo que pioda el programa.
            #self.db.close()
            #self.cursor.close()
            return IdTransaccionParcial
        else:
            #self.db.close()
            #self.cursor.close()
            return None
        
    def conectarrTrs(self):
        return self.db
    
    def cerrarConexiones(self):
        self.db.close()
        self.cursor.close()
    

        
        
        
        

        
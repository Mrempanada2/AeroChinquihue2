from modelo.usuarioTransaccion import UsuarioTransaccion
from BasesDeDatos import Bdd as con

class usuarioDataT():
    
    def __init__(self, usuarioIdTablaParcial):
        #Reutilizar conexion de BddVuelos para la abse de AeroChinVuelos
        self.usuarioID = usuarioIdTablaParcial
        #Crear cursor para interactuar con la base de datos
        self.devolverDatos()
            
        
    def devolverDatos(self):
        con1 = con.Conexion().conectarr()
        with con1:
            cursor = con1.cursor()
            consulta = """SELECT * FROM vuelosEncomiendasParciales WHERE id = ?"""
            cursor.execute(consulta,(int(self.usuarioID),))
        
            Fila_Tr = cursor.fetchone()
        
            if Fila_Tr:
                return Fila_Tr  
            else:
                print("No se haya... error, en data usuarioDataT")
                return None

    

        
        
        
        

        
import sqlite3
from BasesDeDatos import BddVuelos as cn
from interfacesG import vuelos as conP

class CalcularPrecios():
    
    def __init__(self,usuarioID,vuelo,encomienda):
        self.Descuento = False
        self.estaID = usuarioID
        self.EsVuelo = vuelo
        self.EsEncomienda = encomienda
        try:
            self.conexionDatosUsuario = sqlite3.connect("BasesDeDatos/AeroChin.db")
            self.conexionBddParcial = cn.ConexionBddVuelosP().conectarTablaVuelosP()
            #self.conexionBddFinal = sqlite3.connect("BasesDeDatos/AeroChinquihuePagosFinal.db")
            self.conexionBddPrecios = sqlite3.connect("BasesDeDatos/PreciosAeroChin.db")
            self.conexionBddTriple= sqlite3.connect("BasesDeDatos/HorariosVuelos.db")
            self.coneccs = conP.Vuelos(self.estaID).devolverConexionP()
            ##SE ABRE LA CONEXION Y SE CIERRA CUANDO SE HAGAN LOS IF..
            self.realizarOperacion()
            
        except Exception as e:
            print(f"Error al hayar las tablas de datos {e}")
        #finally:
            #self.cerrarConexiones()
            #print("Se cerraron las conexiones.")
    
    def realizarOperacion(self):
        if self.EsVuelo == 1 and self.EsEncomienda == 0:
            self.getDatosUsuario()
            if self.getVueloParcial():
                self.comprobarDisponibilidadV()
        elif self.EsEncomienda == 1 and self.EsVuelo == 0:
            self.getDatosUsuario()
            if self.getEncomiendaParcial():
                self.comprobarDisponibilidadE()
        else:
            print("No es un vuelo ni encomienda, que parametro le pasaste?")
        
    def cerrarConexiones(self):
        self.conexionDatosUsuario.close()
        self.conexionBddParcial.close()
        #self.conexionBddFinal.close()
        self.conexionBddPrecios.close()
        self.conexionBddTriple.close()
        self.coneccs.close()
        
    
            
    #Obtener la Informacion del usuario (cantidad de vuelos,Personal de emergencia, y modificar la cantidad De vuelos si se toma el vuelo)
    def getDatosUsuario(self):
        conexion1 = self.conexionDatosUsuario.cursor()       
        conexion1.execute("""SELECT * FROM usuarios WHERE id = ?""", (self.estaID,))
        fila_usuarios = conexion1.fetchone()
        if fila_usuarios:
            self.esPersonalEmergencias=(fila_usuarios[5])
        
        #Si el usuario tiene mas de 10 vuelos, asignar descuento como TRUE
        if fila_usuarios[4]>=10:
            self.Descuento = True
        
    
    #Obtener la informacion del vuelo que se pretende tomar
    def getVueloParcial(self):
        
        conexion2 = self.conexionBddParcial.cursor()
        conexion2.execute("""SELECT * FROM vuelosp WHERE id = ?""",(self.estaID,))
        fila = conexion2.fetchone()
        if fila:
            self.DestinoV=(fila[1])
            self.AvionV=(fila[2])
            self.IdVueloV=(fila[6])
        
            conexion2.execute("""DELETE  FROM vuelosp WHERE id = ?""",(self.estaID,))
            self.conexionBddParcial.commit()
            print(f"Se extrayeron los datos y las filas de {self.estaID} fueron borradas exitosamente.")
            print(f"ID del vuelo: {self.IdVueloV}")
        else:
            print("No se encontro la fila con la id proporcionada.")
            
    def devolverTipoAvion(self):
        conexion2 = self.conexionBddParcial.cursor()
        conexion2.execute("""SELECT * FROM vuelosp WHERE id = ?""",(self.estaID,))
        fila = conexion2.fetchone()
        if fila:
            AvionV =(fila[2])
            return AvionV

        else:
            print("No se hayo informacion para esa id")
            return None
    
    def getEncomiendaParcial(self):
        
        conexion2 = self.conexionBddParcial.cursor()
        conexion2.execute("""SELECT * FROM vuelosp WHERE id = ?""",(self.estaID,))
        fila = conexion2.fetchone()
        if fila:
            self.DestinoE=(fila[1])
            self.AvionE=(fila[2])
            self.KilosE=(fila[5])
            self.IdVueloE=(fila[6])
            
            print(f"Destino es {self.Destino} y Avion es {self.Avion}")
        
            self.conexion2.execute("""DELETE  FROM vuelosp WHERE id = ?""",(self.estaID,))
            self.conexionBddParcial.commit()
            print(f"Se extrayeron los datos y las filas de {self.estaID} fueron borradas exitosamente.")

            
        else:
            print("No se encontro la fila con la id proporcionada.")
        
            
    def comprobarDisponibilidadE(self):
        conexion3 = self.conexionBddPrecios.cursor()
        conexion3.execute(f"""SELECT {self.Destino} FROM preciosDisp WHERE TAvion = ?""",(self.Avion,))
        Precio = conexion3.fetchone()
        print(f"Buscando precio por kilo para destino: {self.Destino} y avión: {self.Avion}")

        if Precio:
            print (f"El precio por kilo es de {Precio[0]}")
            self.precioEncomienda = Precio
        else:
            print("No se hayo precio ahí")


    #Hayar disponibilidad en los vuelos--encomienda
    def comprobarDisponibilidadV(self):
        conexion3 = self.conexionBddPrecios.cursor()
        conexion3.execute(f"""SELECT {self.Destino} FROM preciosDisp WHERE TAvion = ?""",(self.Avion,))
        Precio = conexion3.fetchone()
        print(f"Buscando precio para destino: {self.Destino} y avión: {self.Avion}")

        if Precio:
            print (f"El precio es de Precio {Precio[0]}")
            precioVuelo = Precio[0]
        else:
            print("No se hayo precio ahí")
            
        if self.Descuento:
            precioVuelo = precioVuelo-precioVuelo*(1/10)
            print(f"\n El usuario es cliente frecuente asi que paga: {precioVuelo}")
        elif self.esPersonalEmergencias:
            pass
            ##Llamar a la funcion de emergencias que genere una posiblidad de evento de emergencia para establecer
            ##el precio en 0 para este usuario.

        
        
    
    
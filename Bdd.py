import sqlite3

class Conexion():
    
    def __init__(self):
        #Crear variable de instancia para conectarse a la base de datos si no existe (crearTablaDatos) y manejar errores
        try:
            self.cno = sqlite3.connect("AeroChin.db")
            self.crearTablaDatos()
        except Exception as e:
            print(e)  
    
    #Crear tabla de datos
    def crearTablaDatos(self):
        
        #Usaremos Sql para hacer una plantilla para la creacion de la tabla en la base de datos
        #Si no esxiste usuarios: id(int que aumenta),nombre(texto) usuario (texto unico por columna) contraseña (texto)
        #Esta es la plantilla:
        tablaUsersSQL = """ CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        contrasena TEXT,
        cantVuelos INTEGER DEFAULT 0,
        pEmergencia INTEGER DEFAULT 0,
        administrador INTEGER DEFAULT 0) """
        
        #Conexion para ejecutar la consulta (cno) usando un cursor para interactuar con la base de datos
        #por medio de una conexion
        curs = self.cno.cursor()
        curs.execute(tablaUsersSQL)
        curs.close()
        self.crearAdmin()
        
    #Crear admin, usuario por defecto
    def crearAdmin(self):
        try:
        
            #Usaremos Sql para insertar los datos de un usuario admin en la base de datos       
            tablaInsertUser = """ INSERT INTO usuarios (nombre, usuario, contrasena, administrador) VALUES (?, ?, ?, ?)"""
            values = ("Administrador", "Admin", "admin123", 1)
                    
            #Conexion para ejecutar la consulta (cno) usando un cursor para interactuar con la base de datos    
            #por medio de una conexion
            curs = self.cno.cursor()
            curs.execute(tablaInsertUser, values)
            #Confirmar insercion del usuario admin
            self.cno.commit()
            #self.cno.close() #Aqui intento un close aver si se soluciona
        except Exception as e:
            print("El usuario admin ya habia sido creado,codigo A",e)
    
    #Retorno de "conexion" para usarla primero en usuarioD
    def conectarr(self):
        return self.cno

        
        

        

    
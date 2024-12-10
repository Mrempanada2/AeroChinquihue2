import sqlite3

class ConexionPrecios():
    
    def __init__(self):

        try:
            self.con3 = sqlite3.connect("PreciosAeroChin.db")
        except Exception as e:
            print(e)
    
    def conexionPrecios(self):
        return self.con3
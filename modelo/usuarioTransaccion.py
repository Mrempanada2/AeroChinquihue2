class UsuarioTransaccion():
    def __init__(self,id="", Destino="",tipoAvion="", Vuelo=0, Encomienda=0, kilos=0, id_pasaje=None):
        #atributos "privados", usar "_"
        self._id = id
        #self._usuario = usuario
        self._destino = Destino
        self._tipoAvion = tipoAvion
        self._vuelo = Vuelo
        self._encomienda = Encomienda    
        self._kilos = kilos
        self._id_pasaje= id_pasaje   
        #REVISAR ID:
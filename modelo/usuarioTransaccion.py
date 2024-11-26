class UsuarioTransaccion():
    def __init__(self,id=None, Destino="",tipoAvion="", Vuelo=0, Encomienda=0, pagado=0, id_pasaje=None):
        #atributos "privados", usar "_"
        self._id = id
        #self._usuario = usuario
        self._destino = Destino
        self._tipoAvion = tipoAvion
        self._vuelo = Vuelo
        self._encomienda = Encomienda    
        self._pagado = pagado
        self._id_pasaje= id_pasaje   
        #REVISAR ID:
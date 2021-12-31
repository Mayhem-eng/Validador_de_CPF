from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False
    
    def conectar(self):
        if not self._ligado:
            error = f"NÃO ESTÁ LIGADO"
            print(error)
            self.log_error(error)
            return
        
        if self.conectado:
            error = f"JÁ ESTÁ CONECTADO!!"
            print(error)
            self.log_error(error)
            return
        

        info = f"{self._nome} ESTÁ CONECTADO"
        print(info)
        self.log_info(info)
        self.conectado = True
        

    def desconectar(self):
        if not self.conectado:
            error = f"{self._nome} NÃO ESTÁ CONECTADO"
            print(error)
            self.log_error(error)
            return
        
        info = f"{self._nome} FOI DESLIGADO!!"
        print(info)
        self.log_info(info)
        self.conectado = False

import Jugador
import utils

class Moderador:
    def __init__(self,jugador1,jugador2):
        self.jugador1 : Jugador = jugador1
        self.jugador2 : Jugador = jugador2
   
        
        self.puntuacioJ1 = 0
        self.puntuacioJ2 = 0
        
        
    def moderar(self):
        if self.jugador1.ma == utils.pedra and self.jugador2.ma == utils.tisores or self.jugador1.ma == utils.tisores and self.jugador2.ma == utils.paper or self.jugador1.ma == utils.paper and self.jugador2.ma == utils.pedra:
            self.puntuacioJ1 +=1
            return f"Guanya {self.jugador1.nom}"
        elif self.jugador2.ma == utils.pedra and self.jugador1.ma == utils.tisores or self.jugador2.ma == utils.tisores and self.jugador1.ma == utils.paper or self.jugador2.ma == utils.paper and self.jugador1.ma == utils.pedra:
            self.puntuacioJ2 +=1
            return f"Guanya {self.jugador2.nom}"
        else:
            return "Empate"

        


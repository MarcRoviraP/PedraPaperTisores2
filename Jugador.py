import random
import utils

class Jugador:
    def __init__(self,nom):
        self.nom = nom
        self.ma = ""
    def get_nom(self):
        return self.nom
    
    def jugar_una_ma(self):
        match(int(random.random()*3)):
            case 0: self.ma = utils.pedra
            case 1: self.ma = utils.paper
            case 2: self.ma = utils.tisores
    
    def asignar_una_ma(self,ma):
        self.ma = ma    
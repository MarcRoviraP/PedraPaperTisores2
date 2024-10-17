import Jugador
import Moderador

def guanyaPartida(nom):
    print(f"{nom} guanya la partida")
    
class game():
    
    def __init__(self):
        
        self.resetPartida("Player","Bot123")

    def resetPartida(self,player,bot):
        
        self.j1 = Jugador.Jugador(player)
        self.j2 = Jugador.Jugador(bot)
        self.mod = Moderador.Moderador(self.j1,self.j2)
        
    def getJ2Ma(self):
        return self.j2.ma
    def juarPartida(self,ma):


        self.j1.asignar_una_ma(ma)
        self.j2.jugar_una_ma()


        self.mod.jugador1 = self.j1
        self.mod.jugador2 = self.j2
        self.mod.moderar()

        
    def determinarGuanyador(self):
    # Abre el archivo CSV en modo lectura
        with open("csv/resultats.csv", "r") as document:
            linies = document.readlines()
            linies = [i.replace("\n", "") for i in linies]

        # Determina el ganador y actualiza las líneas correspondientes
        if self.mod.puntuacioJ1 > self.mod.puntuacioJ2:
            num = int(linies[1].split(",")[1]) + 1  # Obtiene el número de partidas ganadas por el jugador
            linies[0] = f"Partides guañades per maquina,{num}"  # Actualiza la línea
            ganador = self.mod.jugador1.nom
        elif self.mod.puntuacioJ2 > self.mod.puntuacioJ1:
            num = int(linies[0].split(",")[1]) + 1  # Obtiene el número de partidas ganadas por el jugador
            linies[1] = f"Partides guañades per jugador,{num}"  # Actualiza la línea
            ganador = self.mod.jugador2.nom
        else:
            num = int(linies[2].split(",")[1]) + 1  # Obtiene el número de partidas empatadas
            linies[2] = f"Total partides empatades,{num}"  # Actualiza la línea
            ganador = "EMPATE"

        # Escribe los resultados actualizados de nuevo en el archivo CSV
        with open("csv/resultats.csv", "w") as document:
            document.write("\n".join(linies) + "\n")  # Escribe las líneas actualizadas

        return ganador







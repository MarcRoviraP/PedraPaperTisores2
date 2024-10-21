import os
import partida
import utils as ut
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QMenu,
                             QAction, QMessageBox, QMainWindow, QVBoxLayout,
                             QGridLayout, QHBoxLayout, QWidget, QLabel, QLineEdit,
                             QTabWidget, QToolBar, QStatusBar, QInputDialog)
from PyQt5 import QtWidgets
import qdarktheme

game = partida.game()

 
class info():
    def __init__(self,linea):
        self.llistaFin = []
        llista = linea.split(",")
        
        fecha = llista[0]
        separat = fecha.split(" ")
        
        hores = separat[0].replace("-","/")
        
        fin = f"{hores} {separat[1]}"
        
        self.llistaFin.append (fin)
        self.llistaFin.append(llista[1])
        self.llistaFin.append(llista[2])
        self.llistaFin.append(llista[3])
def llegir(ruta):
    document = open(ruta,"r")

    linies = document.readlines()
    linies = [i.replace("\n","") for i in linies]
    document.close()
    
    return linies



class llegirLog(QtWidgets.QMainWindow):
       
     def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)

        # Crear un widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Crear un layout vertical
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Crear la tabla
        self.table_widget = QTableWidget()
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
    
        
        self.table_widget.setWordWrap(False)
        #self.table_widget.setTextElideMode(Qt.ElideRight)# Qt.ElideNone


        self.layout.addWidget(self.table_widget)

        # Configurar la tabla
        linies = llegir("csv/ranking.csv")
        self.llistaObjectes = []
        for linea in linies:
                    
            obj = info(linea)
            self.llistaObjectes.append(obj)
        
        self.table_widget.setRowCount(len(self.llistaObjectes))  # Número de filas
        self.table_widget.setColumnCount(4)  # Número de columnas
        self.table_widget.setHorizontalHeaderLabels(["Data", "Jugador", "Màquina","Rondes"])
                

            # Agregar datos a la tabla
        for row in range(len(self.llistaObjectes)):
            obj = self.llistaObjectes[row].llistaFin
            for i in range(len(obj)):
                item = QTableWidgetItem(obj[i])
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter | Qt.AlignHCenter)  
                self.table_widget.setItem(row, i, item)
                

        # Ajustar el tamaño de las columnas
        for i in range(6):
            self.table_widget.setColumnWidth(i, 150)  
            
        for row in range(len(self.llistaObjectes)):
            self.table_widget.setRowHeight(row, 40)  
            
    
class utils():
    size = 100


class MiLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(20)
        font.setFamily("Roboto")
        self.setFont(font)
class MiLabel(QLabel):
    def __init__(self,txt=""):
        super().__init__()
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(60)
        font.setFamily("Roboto")
        self.setText(txt)
        self.setFont(font)
        
class MiButton(QPushButton):
    def __init__(self,txt = "",key=""):
        super().__init__()
        self.setFixedSize(utils.size,utils.size)    
        icono = QIcon(txt) 
        self.setIconSize(QSize(utils.size,utils.size))
        self.setIcon(icono)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        if key != "":
            self.setShortcut(key)
        
class MainWindow(QMainWindow):
       
    def __init__(self):
        super().__init__()
        
        buttonReload = QAction(QIcon(os.path.join(os.path.dirname(__file__),"reload.png")),"&Recargar",self)
        
        buttonReload.triggered.connect(lambda: self.reload(game.j1.nom,game.j2.nom))
        
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setMovable(False)
        
        toolbar.addAction(buttonReload)
        self.addToolBar(toolbar)
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)
        
        self.a = None
        self.setWindowTitle("Pedra Paper Tisores")
        
        self.showMaximized()
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(False)
        
        tabs.addTab(self.cargarStart(),"Joc")
        tabs.addTab(self.cargarEstadistiques(),"Estadistiques")

        
        self.setCentralWidget(tabs)
        
        
        buttonActionReiniciar = QAction(
            "&Reiniciar",self
        )
        buttonActionReiniciar.triggered.connect(lambda: self.reset(game.j1.nom,game.j2.nom))
        buttonActionRondes = QAction(
            "&Rondes",self
        )
        buttonActionRondes.triggered.connect(lambda: self.cambiarNumRondes())
        
        menu = self.menuBar()
        file_menu =menu.addMenu("&Ajustes")
        file_menu.addAction(buttonActionReiniciar)
        file_menu.addAction(buttonActionRondes)
        
    def onContextMenu(self,pos):
        fosc = QAction("Tema Fosc", self)
        clar = QAction("Tema Clar", self)
        detalls = QAction("Detalls del registres", self)
        
        fosc.triggered.connect(lambda checked: self.oscur())
        clar.triggered.connect(lambda checked: self.clar())
        detalls.triggered.connect(lambda checked: self.obrirDetalls())
        
        context = QMenu(self)
        context.addAction(fosc)
        context.addAction(clar)
        context.addAction(detalls)
        context.exec_(self.mapToGlobal(pos))
        
    
    def clar(self):
        qdarktheme.setup_theme("light")
    def oscur(self):
        qdarktheme.setup_theme()
        
    def obrirDetalls(self):
        
        if self.a is None:
            self.a = llegirLog()
            self.a.setWindowTitle("Detalles del Registro")  # Establece un título para la ventana
            self.a.resize(1000, 1000)  # Ajusta el tamaño de la ventana si es necesario
            self.a.show()  # Muestra la ventana
        else:
            self.a.show()
            self.a.raise_()  # Si la ventana ya existe, la trae al frente

        

    def cargarEstadistiques(self):
        
        document = open("csv/resultats.csv","r")

        linies = document.readlines()
        linies = [i.replace("\n","") for i in linies]
        linies = [i.replace(",",":  ") for i in linies]
        document.close()
        
        resul = "\n".join(linies) 
        
        res = QLabel(resul)
       
        
        layout = QVBoxLayout()
        layout.addWidget(res)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        return widget
    def cargarStart(self):
        1
        win = QDialog(
            
        )
        
        gridPane = QGridLayout()

        # Crear y estilizar los campos de entrada
        editPlayer = MiLineEdit()
        editPlayer.setPlaceholderText("Insertar nombre usuario:")
        editPlayer.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #5D5D5D;
                border-radius: 10px;
                font-size: 16px;
            }
            QLineEdit::placeholder {
                color: #A9A9A9;
            }
        """)

        editBot = MiLineEdit()
        editBot.setPlaceholderText("Insertar nombre del rival:")
        editBot.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #5D5D5D;
                border-radius: 10px;
                font-size: 16px;
            }
            QLineEdit::placeholder {
                color: #A9A9A9;
            }
        """)

        # Crear y estilizar el botón
        ready = MiButton()
        ready.setText("PREPARADO")
        ready.setFixedWidth(200)
        ready.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)

        # Conectar el botón a la funcionalidad
        ready.clicked.connect(lambda: self.reload(editPlayer.text(), editBot.text()))

        # Agregar los widgets al layout
        gridPane.addWidget(editPlayer, 0, 0)
        gridPane.addWidget(editBot, 1, 0)
        gridPane.addWidget(ready, 2, 0)

        # Ajustar el espaciado y las alineaciones
        gridPane.setContentsMargins(50, 50, 50, 50)  # Márgenes externos
        gridPane.setSpacing(20)  # Espacio entre elementos

        widget = QWidget()
        widget.setLayout(gridPane)

        # Devolver el widget con layout ajustado
        return widget

        
    def cargarMainWidget(self):
    
        self.contRound = 0


        mainPane = QVBoxLayout()
        hBoxTop = QGridLayout()
        hBox = QHBoxLayout()
        
        
        hBox.setSpacing(10)
        hBox.setAlignment(Qt.AlignBottom)
        
        self.contador = QLabel("0")
        self.contador.setText(f"Ronda {self.contRound} de {str(ut.rondes)}")
        self.contador.setAlignment(Qt.AlignRight)
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.statusBar.addWidget(self.contador,1)
        
        piedra = MiButton(f"{ut.pedra}.png","1")
        piedra.clicked.connect(lambda: self.click(ut.pedra))
        
        paper = MiButton(f"{ut.paper}.png","2")
        paper.clicked.connect(lambda: self.click(ut.paper))
        
        tijera = MiButton(f"{ut.tisores}.png","3")
        tijera.clicked.connect(lambda: self.click(ut.tisores))
        

        
        hBox.addStretch()
        hBox.addWidget(piedra)
        hBox.addWidget(paper)
        hBox.addWidget(tijera)
     
     
        hBox.addStretch()
           
        self.labelBot = MiLabel(game.j2.nom)
        self.labelBot.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignBottom)

        hBoxTop.addWidget(self.labelBot,0,0)
        self.imageBot = MiLabel()
        self.imageBot.setPixmap(QPixmap(f"{ut.paper}_default.png"))      
        hBoxTop.addWidget(self.imageBot,1,0)
        
        
        self.labelPlayer = MiLabel(game.j1.nom)
        self.labelPlayer.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignBottom)
        hBoxTop.addWidget(self.labelPlayer,0,1)
        self.imagePlayer = MiLabel()
        self.imagePlayer.setPixmap(QPixmap(f"{ut.tisores}_default.png"))
        hBoxTop.addWidget(self.imagePlayer,1,1)
    
        hBoxTop.setAlignment(Qt.AlignHCenter)
        hBoxTop.setSpacing(200)

        mainPane.addLayout(hBoxTop)
        mainPane.addLayout(hBox)
        
        widget = QWidget()

      
        widget.setLayout(mainPane)
        return widget
    
    def click(self,ma):
        
        self.contRound +=1
        self.contador.setText(f"Ronda {self.contRound} de {str(ut.rondes)}")

        self.imagePlayer.setPixmap(QPixmap(f"{ma}_default.png"))
        
        game.juarPartida(ma)

        self.imageBot.setPixmap(QPixmap(f"{game.getJ2Ma()}_default.png"))
        
        
        self.labelPlayer.setText(f"{str(game.j1.nom)} {game.mod.puntuacioJ1}")
        self.labelBot.setText(f"{str(game.j2.nom)} {game.mod.puntuacioJ2}")
        
        winCont = 3
        if game.mod.puntuacioJ2 == winCont or game.mod.puntuacioJ1 == winCont or self.contRound == ut.rondes:
            
            guañador = game.determinarGuanyador()
            
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Felicidades")
            dlg.setText(f"Felicidades ha ganado {guañador}")
            dlg.exec()
            winLabel = MiLabel(f"{guañador}")
            winLayout = QGridLayout()
            
            winLayout.addWidget(winLabel)
            
            reloadBtn = MiButton("reload.png","R")
            reloadBtn.clicked.connect(lambda: self.reload(game.j1.nom,game.j2.nom))
            reloadBtn.setFixedSize(300,300)
            winLayout.addWidget(reloadBtn)            
            winLayout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.widget2 = QWidget()
            self.widget2.setLayout(winLayout)
            
            self.setCentralWidget(self.widget2)
            game.resetPartida(game.j1.nom,game.j2.nom)
            
    def reset(self,player,bot):
        self.reload(player,bot)
        game.resetPartida(player,bot)
        
    def cambiarNumRondes(self):
        

        rondas,value = QInputDialog.getInt(
            self,
            "Seleccionar rondas",
            "Introduce el numero de rondas entre 5 - 15",
            value=ut.rondes,
            min=5,
            max=15,
            step=1
        )        
        
        ut.rondes = rondas if value else ut.rondes
        
        self.reset(game.j1.nom,game.j2.nom)
        
        
    def reload(self,player,bot):
        self.close()
        self.__init__
      
        
        player = "Player" if player == "" else str(player)
        bot = "Bot123" if bot == "" else str(bot)
        game.j1.nom = player
        game.j2.nom = bot
        
        self.setCentralWidget(self.cargarMainWidget())
        self.show()

        


app = QApplication([])
window = MainWindow()

#QPalette
qdarktheme.setup_theme()
window.setStyleSheet("QMainWindow{background-color: #5cb0df}")
window.show()

app.exec_()

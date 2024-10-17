from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)

class info():
    def __init__(self,linea):
        self.llistaFin = []
        llista = linea.split(",")
        self.llistaFin.append (llista[0])
        self.llistaFin.append(llista[1])
        self.llistaFin.append(llista[2])
        self.llistaFin.append(llista[3])
def llegir(ruta):
    document = open(ruta,"r")

    linies = document.readlines()
    linies = [i.replace("\n","") for i in linies]
    document.close()
    
    return linies


class MainWindow(QtWidgets.QMainWindow):
       
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
            
    

            
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()


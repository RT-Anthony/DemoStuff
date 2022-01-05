import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

import mediator

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, bus):
        QtWidgets.QMainWindow.__init__(self)
        self.bus = bus
        self.setWindowTitle("App Scale Demo")

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QtWidgets.QAction("Exit", self) 
        exit_action.setShortcut(QtGui.QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        self.status = self.statusBar()
        self.status.showMessage("Data Loaded")

        self.setFixedSize(500, 500)
        self.bus.notify(self, "SETUP")

        self.init_ui()

    def init_ui(self):
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)

class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.main_window = parent
        self.layout = QtWidgets.QVBoxLayout(self)

        self.button1 = QtWidgets.QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QtWidgets.QPushButton("Button 2")
        self.layout.addWidget(self.button2)
        
        self.connect_signals()

    def connect_signals(self):
        self.button1.clicked.connect(self.button_1)
        self.button2.clicked.connect(self.button_2)

    def button_1(self):
        self.main_window.bus.notify(self, "BUTTON1")

    def button_2(self):
        self.main_window.bus.notify(self, "BUTTON2")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    bus = mediator.MessageBus()
    window = MainWindow(bus)
    bus.notify(None, "Constructed Window")
    window.show()
    sys.exit(app.exec_())

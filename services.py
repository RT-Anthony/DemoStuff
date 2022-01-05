from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
import webbrowser

class Service(object):
    def notify(self, sender, message):
        print("{} sent {}".format(sender, message))

class MainService(Service):
    def notify(self, sender, message):
        if message == "BUTTON1":
            print("Do Button1 things")
        if message == "BUTTON2":
            print("Do Button2 things")


class HelpService(Service):
    def notify(self, sender, message):
        if message == "SETUP":
            sender.help_menu = sender.menu.addMenu("Help")
            sender.bus.notify(sender, "HELP")

class GoogleService(Service):
    def notify(self, sender, message):
        if message == "HELP":
            help_action = QtWidgets.QAction("help me", sender)
            help_action.triggered.connect(self.help)

            sender.help_menu.addAction(help_action)

    def help(self):
        webbrowser.open("google.com", new=1, autoraise=True)

class MainServiceUpdate(Service):
    def notify(self, sender, message):
        if message == "BUTTON1":
            print("Do Button1 post-process things")
        if message == "BUTTON2":
            print("Do Button2 post-process things")

class DockService(Service):
    def notify(self, sender, message):
        if message == "SETUP":
            self.bus = sender.bus
            dock = QtWidgets.QDockWidget("Another button", sender)
            dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea | QtCore.Qt.TopDockWidgetArea)
            button3 = QtWidgets.QPushButton("Button 3")
            dock.setWidget(button3)
            sender.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            button3.clicked.connect(self.button_3)

    def button_3(self):
        self.bus.notify(self, "BUTTON3")

import tkinter
from tkinter import *
from tkinter.ttk import *

from PyQt5.QtWidgets import QMainWindow, QApplication

from alarm import alarm
from playsound import playsound
from losi import *
import sys
from PySide6 import QtCore
class myStub(tkinter.Tk):
    def __init__(self):
        super(myStub, self).__init__()
        self.geometry("200x200")
        self.label = Label(self,
                      text="This is the Alarm Stub")

        self.label.pack(pady=10)
        # a button widget which will open a
        # new window on button click
        self.btn = Button(self,
                     text="Raise Alarm",
                     command=self.openNewWindow)
        self.btn.pack(pady=10)
        self.btn2 = Button(self,
                          text="openthat",
                          command=self.openReports)
        self.btn2.pack(pady=10)
        # mainloop, runs infinitely

        mainloop()

    def openNewWindow(self):

        global newWindow
        newWindow = alarm()

        try:
            self.after(5000, self.deestroy())
        except:
            print("exception")


    def deestroy(self):
        newWindow.destroy()

    def openReports(self):
        print("in Reports Gui")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())


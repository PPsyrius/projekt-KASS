import os
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import QObject
from PySide2.QtGui import QPaintDevice, QIcon

## Message Boxes ##
def CreateErrorMSGBox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowIcon(QIcon('icon64.png'))
    msg.setText(text)
    msg.setWindowTitle("Error")
    msg.exec_()

def CreateStatusMSGBox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowIcon(QIcon('icon64.png'))
    msg.setText(text)
    msg.setWindowTitle("Status")
    msg.exec_()

def CreateDetailedErrorMSGBox(text,detailed_text,informative_text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowIcon(QIcon('icon64.png'))
    msg.setText(text)
    msg.setInformativeText(informative_text)
    msg.setDetailedText(detailed_text)
    msg.setWindowTitle("Error")
    msg.exec_()

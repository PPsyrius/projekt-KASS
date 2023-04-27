# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

## Message Boxes ##
def CreateErrorMSGBox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowIcon(QIcon('icon64.png'))
    msg.setText(text)
    msg.setWindowTitle("Error")
    msg.exec()

def CreateStatusMSGBox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowIcon(QIcon('icon64.png'))
    msg.setText(text)
    msg.setWindowTitle("Status")
    msg.exec()

def CreateDetailedErrorMSGBox(text,detailed_text,informative_text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowIcon(QIcon('icon64.png'))
    msg.setText(text)
    msg.setInformativeText(informative_text)
    msg.setDetailedText(detailed_text)
    msg.setWindowTitle("Error")
    msg.exec()

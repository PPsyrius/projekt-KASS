# This Python file uses the following encoding: utf-8
import sys
import os
import datetime

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTableView
from PySide2.QtCore import QFile, QTimer
from PySide2.QtUiTools import QUiLoader

username_read = "Stranger"

class UI_form_main(QWidget):
    def __init__(self):
        super(UI_form_main, self).__init__()
        self.load_ui()

        self.lb_welcome = self.findChild(QLabel, 'lb_welcome')
        self.lb_currentDateTime = self.findChild(QLabel, 'lb_currentDateTime')
        self.bt_addCourse = self.findChild(QPushButton, 'bt_addCourse')
        self.bt_removeCourse = self.findChild(QPushButton, 'bt_removeCourse')
        self.bt_generateTable = self.findChild(QPushButton, 'bt_generateTable')
        self.bt_exportPDF = self.findChild(QPushButton, 'bt_exportPDF')
        self.bt_logOut = self.findChild(QPushButton, 'bt_logOut')
        self.table_wholeSchedule = self.findChild(QTableView, 'table_wholeSchedule')

        self.lb_welcome.setText("Welcome, " + username_read)
        self.lb_currentDateTime.setText(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        self.bt_addCourse.clicked.connect(self.addCourse)
        self.bt_removeCourse.clicked.connect(self.removeCourse)
        self.bt_generateTable.clicked.connect(self.generateTable)
        self.bt_exportPDF.clicked.connect(self.exportPDF)
        self.bt_logOut.clicked.connect(self.logOut)

        timer = QTimer(self)
        timer.timeout.connect(self.updateCurrentTime)
        timer.start(1000)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_main.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateCurrentTime(self):
        self.lb_currentDateTime.setText(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    def addCourse(self, time, profname, date, no_students, name, courseid):
        pass

    def removeCourse(self, courseid):
        pass

    def generateTable(self):
        pass

    def exportPDF(self):
        pass

    def logOut(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    widget = UI_form_main()
    widget.show()
    sys.exit(app.exec_())

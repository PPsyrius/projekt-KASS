# This Python file uses the following encoding: utf-8
import sys
import os
import datetime

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTableView, QLineEdit
from PySide2.QtCore import QFile, QTimer, QAbstractTableModel, Qt
from PySide2.QtUiTools import QUiLoader

from gvar import *
from sqliteDB import *

class UI_form_login(QWidget):
    def __init__(self):
        super(UI_form_login, self).__init__()
        self.load_ui()

        self.setWindowTitle('KMITL Academic Scheduler System: Authentication')
        
        self.lb_logInStatus = self.findChild(QLabel, 'lb_logInStatus')
        self.bt_logIn = self.findChild(QPushButton, 'bt_logIn')
        self.bt_guestAccess = self.findChild(QPushButton, 'bt_guestAccess')
        self.le_email = self.findChild(QLineEdit, 'le_email')
        self.le_password = self.findChild(QLineEdit, 'le_password')

        self.bt_logIn.clicked.connect(self.authenLogIn)
        self.bt_guestAccess.clicked.connect(self.guestLogIn)
        
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_login.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateStatusMessage(self, text):
        self.lb_logInStatus.setText(text)

    def authenLogIn(self):
        email_inp = self.le_email.text()
        password_inp = self.le_password.text()

        login_q = session.query(Professor).filter_by(email=email_inp).first()
        if not login_q:
            self.updateStatusMessage("Status: Mismatched User") # Email not exist
        elif login_q.password == password_inp:
            self.updateStatusMessage("Status: Login Succesful") # Success
            global username_read
            username_read = login_q.fullname
            widget_menu.show()
            widget_login.hide()
        else:
            self.updateStatusMessage("Status: Mismatched User") # Other Errors
            print(password_inp)
            print(login_q.password)

    def guestLogIn(self):
        widget_menu_guest.show()
        widget_login.hide()    

class UI_form_main(QWidget):
    def __init__(self):
        super(UI_form_main, self).__init__()
        self.load_ui()

        self.setWindowTitle('KMITL Academic Scheduler System: ' + username_read )

        self.lb_welcome = self.findChild(QLabel, 'lb_welcome')
        self.lb_currentDateTime = self.findChild(QLabel, 'lb_currentDateTime')
        self.bt_addCourse = self.findChild(QPushButton, 'bt_addCourse')
        self.bt_removeCourse = self.findChild(QPushButton, 'bt_removeCourse')
        self.bt_generateTable = self.findChild(QPushButton, 'bt_generateTable')
        self.bt_exportPDF = self.findChild(QPushButton, 'bt_exportPDF')
        self.bt_logOut = self.findChild(QPushButton, 'bt_logOut')
        self.table_wholeSchedule = self.findChild(QTableView, 'table_wholeSchedule')

        self.lb_welcome.setText("Welcome, " + username_read )
        self.lb_currentDateTime.setText(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        self.bt_addCourse.clicked.connect(self.addCourse)
        self.bt_removeCourse.clicked.connect(self.removeCourse)
        self.bt_generateTable.clicked.connect(self.generateTable)
        self.bt_exportPDF.clicked.connect(self.exportPDF)
        self.bt_logOut.clicked.connect(self.logOut)

        timer = QTimer(self)
        timer.timeout.connect(self.updateCurrentTime)
        timer.start(1000)

        self.updateTable()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_main.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateCurrentTime(self):
        self.lb_currentDateTime.setText(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        self.updateDB()

    def updateDB(self):
        self.setWindowTitle('KMITL Academic Scheduler System: ' + username_read )
        self.lb_welcome.setText("Welcome, " + username_read )

    def updateCourseList(self):
        global courseTableList
        courseTableList = []
        for c in session.query(Course).order_by(Course.courseid).filter_by(profname=username_read):
            c_done = []
            c_done.extend([c.courseid,c.name,c.no_students])
            c_done.extend([date[c.date-1],time[c.time-1],c.profname])
            courseTableList.append(c_done)

    def addCourse(self):
        self.updateCourseList()
        pass

    def removeCourse(self):
        self.updateCourseList()
        widget_course_remove.show()
        widget_menu.hide()

    def updateTable(self):
        table_model = MyTableModel(self, scheduleTableList, scheduleHeader)
        self.table_wholeSchedule.setModel(table_model)

    def generateTable(self):
        self.updateTable()
        pass

    def exportPDF(self):
        print(username_read)
        pass

    def logOut(self):
        global username_read
        username_read = "Guest"
        widget_login.show()
        widget_menu.hide()


class UI_form_main_guest(QWidget):
    def __init__(self):
        super(UI_form_main_guest, self).__init__()
        self.load_ui()

        self.setWindowTitle('KMITL Academic Scheduler System: Guess View')

        self.lb_welcome = self.findChild(QLabel, 'lb_welcome')
        self.lb_currentDateTime = self.findChild(QLabel, 'lb_currentDateTime')
        self.bt_exportPDF = self.findChild(QPushButton, 'bt_exportPDF')
        self.bt_logOut = self.findChild(QPushButton, 'bt_logOut')
        self.table_wholeSchedule = self.findChild(QTableView, 'table_wholeSchedule')

        self.lb_welcome.setText("Welcome, " + username_read)
        self.lb_currentDateTime.setText(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        self.bt_exportPDF.clicked.connect(self.exportPDF)
        self.bt_logOut.clicked.connect(self.logOut)

        timer = QTimer(self)
        timer.timeout.connect(self.updateCurrentTime)
        timer.start(1000)

        self.updateTable()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_main_guest.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateCurrentTime(self):
        self.lb_currentDateTime.setText(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    def updateTable(self):
        table_model = MyTableModel(self, scheduleTableList, scheduleHeader)
        self.table_wholeSchedule.setModel(table_model)

    def exportPDF(self):
        pass

    def logOut(self):
        global username_read
        username_read = "Guest"
        widget_login.show()
        widget_menu_guest.hide()

class UI_course_remove(QWidget):
    def __init__(self):
        super(UI_course_remove, self).__init__()
        self.load_ui()

        self.setWindowTitle('KMITL Academic Scheduler System: Remove Course')

        self.le_courseID = self.findChild(QLineEdit, 'le_courseID')
        self.lb_statusMessage = self.findChild(QLabel, 'lb_statusMessage')
        self.bt_back = self.findChild(QPushButton, 'bt_back')
        self.bt_remove = self.findChild(QPushButton, 'bt_remove')
        self.table_courseList = self.findChild(QTableView, 'table_courseList')

        self.bt_back.clicked.connect(self.previousPage)
        self.bt_remove.clicked.connect(self.removeCourse)

        self.updateStatusMessage("Click Remove Once To Pull Data")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_course_remove.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateStatusMessage(self, text):
        self.lb_statusMessage.setText(text)

    def updateDB(self):
        global courseTableList
        courseTableList = []
        for c in session.query(Course).order_by(Course.courseid).filter_by(profname=username_read):
            c_done = []
            c_done.extend([c.courseid,c.name,c.no_students])
            c_done.extend([date[c.date-1],time[c.time-1],c.profname])
            courseTableList.append(c_done)

    def updateTable(self):
        self.updateDB()

        table_model = MyTableModel(self, courseTableList, courseHeader)
        self.table_courseList.setModel(table_model)
        self.table_courseList.resizeColumnsToContents()

    def removeCourse(self):
        courseID_inp = self.le_courseID.text()

        cd = session.query(Course).filter_by(courseid=courseID_inp).first()
        
        if not courseTableList:
            self.updateStatusMessage("Error: No Course in DB by this User")
        elif courseID_inp=="":
            self.updateStatusMessage("Status: Table Updated") # Pull Data
        elif not cd:
            self.updateStatusMessage("Error: Invalid Course ID") # CourseID not exist
        else:
            self.updateStatusMessage("Status: Course Removed") # Success
            session.delete(cd)
            
        self.updateTable()            
        ##REMOVE_THIS##session.commit()

    def previousPage(self):
        widget_menu.show()
        widget_course_remove.hide()

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

if __name__ == "__main__":
    app = QApplication([])

    widget_menu = UI_form_main()
    widget_menu_guest = UI_form_main_guest()
    widget_login = UI_form_login()
    widget_course_remove = UI_course_remove()

    widget_login.show()
    sys.exit(app.exec_())
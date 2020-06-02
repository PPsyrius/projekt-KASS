# This Python file uses the following encoding: utf-8
import sys
import os
import datetime

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTableView, QLineEdit, QComboBox, QTableWidgetItem
from PySide2.QtCore import QFile, QTimer, QAbstractTableModel, Qt
from PySide2.QtUiTools import QUiLoader

from gvar import *

global username_read
username_read = "Dr Visit"

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
        global username_read

        login_p = session.query(Professor).filter_by(Email=email_inp).first()
        login_a = session.query(Admin).filter_by(Email=email_inp).first()

        if not (login_p or login_a):
            self.updateStatusMessage("Status: Invalid User") # Email not exist
        elif login_a.password == password_inp and login_a.Email == email_inp:
            self.updateStatusMessage("Status: Login Succesful") # Success (Admin)
            username_read = login_a.ProfName
            widget_menu.show()
            widget_login.hide()
        elif login_p.password == password_inp and login_p.Email == email_inp:
            self.updateStatusMessage("Status: Login Succesful") # Success (Professor)
            username_read = login_p.ProfName
            widget_menu_prof.show()
            widget_login.hide()
        else:
            self.updateStatusMessage("Status: Mismatched User") # Other Errors
            print(password_inp)
            print(login_a.password)
            print(login_q.password)

    def guestLogIn(self):
        widget_menu_guest.show()
        widget_login.hide()    


class UI_form_pick_timeslot(QWidget):
    def __init__(self):
        super(UI_form_pick_timeslot, self).__init__()
        self.load_ui()

        self.setWindowTitle('KMITL Academic Scheduler System: Pick Timeslot')

        self.cb_currentSubject = self.findChild(QComboBox, 'cb_currentSubject')
        self.bt_11 = self.findChild(QPushButton, 'bt_11')
        self.bt_21 = self.findChild(QPushButton, 'bt_21')
        self.bt_31 = self.findChild(QPushButton, 'bt_31')
        self.bt_41 = self.findChild(QPushButton, 'bt_41')
        self.bt_51 = self.findChild(QPushButton, 'bt_51')
        self.bt_12 = self.findChild(QPushButton, 'bt_12')
        self.bt_22 = self.findChild(QPushButton, 'bt_22')
        self.bt_32 = self.findChild(QPushButton, 'bt_32')
        self.bt_42 = self.findChild(QPushButton, 'bt_42')
        self.bt_52 = self.findChild(QPushButton, 'bt_52')
        self.bt_back = self.findChild(QPushButton, 'bt_back')
        self.lbb_ProfName = self.findChild(QLabel, 'lbb_ProfName')
        self.lbb_NoStudents = self.findChild(QLabel, 'lbb_NoStudents')
        self.lbb_RoomType = self.findChild(QLabel, 'lbb_RoomType')
        self.lbb_CourseName = self.findChild(QLabel, 'lbb_CourseName')

        self.updateSelectedCourseList()
    
        self.cb_currentSubject.addItems(selectedCourseList)
        self.cb_currentSubject.currentTextChanged.connect(self.CbLoadState)
        self.bt_11.clicked.connect(self.BtToggleState)
        self.bt_21.clicked.connect(self.BtToggleState)
        self.bt_31.clicked.connect(self.BtToggleState)
        self.bt_41.clicked.connect(self.BtToggleState)
        self.bt_51.clicked.connect(self.BtToggleState)
        self.bt_12.clicked.connect(self.BtToggleState)
        self.bt_22.clicked.connect(self.BtToggleState)
        self.bt_32.clicked.connect(self.BtToggleState)
        self.bt_42.clicked.connect(self.BtToggleState)
        self.bt_52.clicked.connect(self.BtToggleState)
        self.bt_back.clicked.connect(self.previousPage)

        self.bt_11.setCheckable(True)
        self.bt_21.setCheckable(True)
        self.bt_31.setCheckable(True)
        self.bt_41.setCheckable(True)
        self.bt_51.setCheckable(True)
        self.bt_12.setCheckable(True)
        self.bt_22.setCheckable(True)
        self.bt_32.setCheckable(True)
        self.bt_42.setCheckable(True)
        self.bt_52.setCheckable(True)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_pick_timeslot.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateSelectedCourseList(self):
        global selectedCourseList
        selectedCourseList = ["--Select Here--"]
        for c in session.query(Course).filter_by(ProfName=username_read).order_by(Course.CourseID):
            selectedCourseList.append(c.CourseID)
        
    def updateDB(self):
        self.lbb_ProfName.setText('-')
        self.lbb_NoStudents.setText('-')
        self.lbb_RoomType.setText('-')
        self.lbb_CourseName.setText('-')

        cID = self.cb_currentSubject.currentText()
        if cID!= "--Select Here--":
            c = session.query(Course).filter_by(CourseID=cID).first()
            self.lbb_ProfName.setText(c.ProfName)
            self.lbb_NoStudents.setText(str(c.NoStudents))
            self.lbb_RoomType.setText(c.RoomType)
            self.lbb_CourseName.setText(c.CourseName)
            
        for c in session.query(Course).filter_by(Course.CourseID):
            c_done = [c.CourseID,c.CourseName,c.NoStudents,c.ProfName,c.RoomType]
            selectedCourseTableList.append(c_done)
            selectedCourseList.append(c.CourseID)

    def CbLoadState(self):
        self.updateDB()

        self.bt_11.setChecked(False)
        self.bt_21.setChecked(False)
        self.bt_31.setChecked(False)
        self.bt_41.setChecked(False)
        self.bt_51.setChecked(False)
        self.bt_12.setChecked(False)
        self.bt_22.setChecked(False)
        self.bt_32.setChecked(False)
        self.bt_42.setChecked(False)
        self.bt_52.setChecked(False)
        
        cID = self.cb_currentSubject.currentText()
        if cID!= "--Select Here--":
            for ts in session.query(CourseTimeSlot).filter_by(CourseID=cID).order_by(CourseTimeSlot.DateTime):
                if ts.DateTime==11:
                    self.bt_11.setChecked(True)
                elif ts.DateTime==21:
                    self.bt_21.setChecked(True)
                elif ts.DateTime==31:
                    self.bt_31.setChecked(True)
                elif ts.DateTime==41:
                    self.bt_41.setChecked(True)
                elif ts.DateTime==51:
                    self.bt_51.setChecked(True)
                elif ts.DateTime==12:
                    self.bt_12.setChecked(True)
                elif ts.DateTime==22:
                    self.bt_22.setChecked(True)
                elif ts.DateTime==32:
                    self.bt_32.setChecked(True)
                elif ts.DateTime==42:
                    self.bt_42.setChecked(True)
                elif ts.DateTime==52:
                    self.bt_52.setChecked(True)
                    
    def BtToggleState(self):
        cID = self.cb_currentSubject.currentText()
        if cID!= "--Select Here--":
            sender = self.sender()
            print(self.sender().text())

            ## Toggle Status ##
            if sender.isChecked():
                sender.setChecked(True)     # Select Timeslot
            else:
                sender.setChecked(False)    # Deselect Timeslot

            if sender == self.bt_11:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=11)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=11).first()
                    session.delete(ctss)
            elif sender == self.bt_21:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=21)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=21).first()
                    session.delete(ctss)
            elif sender == self.bt_31:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=31)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=31).first()
                    session.delete(ctss)
            elif sender == self.bt_41:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=41)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=41).first()
                    session.delete(ctss)
            elif sender == self.bt_51:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=51)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=51).first()
                    session.delete(ctss)
            elif sender == self.bt_12:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=12)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=12).first()
                    session.delete(ctss)
            elif sender == self.bt_22:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=22)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=22).first()
                    session.delete(ctss)
            elif sender == self.bt_32:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=32)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=32).first()
                    session.delete(ctss)
            elif sender == self.bt_42:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=42)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=42).first()
                    session.delete(ctss)
            elif sender == self.bt_52:
                if sender.isChecked():
                    ctss = CourseTimeSlot(CourseID=cID, DateTime=52)
                    session.add(ctss)
                else:
                    ctss = session.query(CourseTimeSlot).filter_by(CourseID=cID).filter_by(DateTime=52).first()
                    session.delete(ctss)

            ##REMOVE_THIS##session.commit()

    def previousPage(self):
        #self.updateTable()
        pass


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

    def addCourse(self):
        widget_course_add.show()
        widget_menu.hide()

    def removeCourse(self):
        widget_course_remove.show()
        widget_menu.hide()

    def updateTable(self):
        newScheduleTableList()
            
        table_model = MyTableModel(self, scheduleTableList, scheduleHeader)
        self.table_wholeSchedule.setModel(table_model)
        self.table_wholeSchedule.resizeColumnsToContents()

    def generateTable(self):
        self.updateTable()
        pass

    def exportPDF(self):
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
        newScheduleTableList()
            
        table_model = MyTableModel(self, scheduleTableList, scheduleHeader)
        self.table_wholeSchedule.setModel(table_model)
        self.table_wholeSchedule.resizeColumnsToContents()

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

    def updateCourseList(self):
        global courseList
        courseList = []
        for c in session.query(Course).order_by(Course.CourseID):
            profList.append(c.CourseID)

    def updateDB(self):
        global courseTableList
        courseTableList = []
        for c in session.query(Course).order_by(Course.CourseID):
            c_done = [c.CourseID,c.CourseName,c.NoStudents,c.ProfName,c.RoomType]
            courseTableList.append(c_done)

    def updateTable(self):
        self.updateDB()

        table_model = MyTableModel(self, courseTableList, courseHeader)
        self.table_courseList.setModel(table_model)
        self.table_courseList.resizeColumnsToContents()

    def removeCourse(self):
        courseID_inp = self.le_courseID.text()

        cd = session.query(Course).filter_by(CourseID=courseID_inp).first()
        
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
        self.updateCourseList()
        ##REMOVE_THIS##session.commit()

    def previousPage(self):
        widget_menu.show()
        widget_course_remove.hide()
        widget_course_add.updateStatusMessage("Click Remove Once To Pull Data")
        widget_course_remove.updateStatusMessage("Click Remove Once To Pull Data")


class UI_course_add(QWidget):
    def __init__(self):
        super(UI_course_add, self).__init__()
        self.load_ui()

        self.setWindowTitle('KMITL Academic Scheduler System: Add Course')

        self.le_courseID = self.findChild(QLineEdit, 'le_courseID')
        self.le_courseName = self.findChild(QLineEdit, 'le_courseName')
        self.le_capacity = self.findChild(QLineEdit, 'le_capacity')
        self.cb_prof = self.findChild(QComboBox, 'cb_prof')
        self.cb_roomtype = self.findChild(QComboBox, 'cb_roomtype')
        self.lb_statusMessage = self.findChild(QLabel, 'lb_statusMessage')
        self.bt_back = self.findChild(QPushButton, 'bt_back')
        self.bt_add = self.findChild(QPushButton, 'bt_add')
        self.table_courseList = self.findChild(QTableView, 'table_courseList')

        self.cb_prof.addItems(profList)
        self.cb_roomtype.addItems(roomType)
        self.bt_back.clicked.connect(self.previousPage)
        self.bt_add.clicked.connect(self.addCourse)

        self.updateStatusMessage("Click Remove Once To Pull Data")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form_course_add.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def updateStatusMessage(self, text):
        self.lb_statusMessage.setText(text)


    def updateCourseList(self):
        global courseList
        courseList = []
        for c in session.query(Course).order_by(Course.CourseID):
            profList.append(c.CourseID)

    def updateDB(self):
        global courseTableList
        courseTableList = []
        for c in session.query(Course).order_by(Course.CourseID):
            c_done = [c.CourseID,c.CourseName,c.NoStudents,c.ProfName,c.RoomType]
            courseTableList.append(c_done)

    def updateTable(self):
        self.updateDB()

        table_model = MyTableModel(self, courseTableList, courseHeader)
        self.table_courseList.setModel(table_model)
        self.table_courseList.resizeColumnsToContents()

    def addCourse(self):
        courseID_inp = self.le_courseID.text()
        courseName_inp = self.le_courseName.text()
        capacity_inp = self.le_capacity.text()
        prof_inp = self.cb_prof.currentText()
        roomtype_inp = self.cb_roomtype.currentText()
        
        if not courseTableList:
            self.updateStatusMessage("Error: No Course in DB by this User")
        elif courseID_inp=="":
            self.updateStatusMessage("Status: Table Updated") # Pull Data
        elif courseID_inp in courseList:
            self.updateStatusMessage("Error: Course ID Exists") # CourseID exists
        elif courseName_inp=="" or capacity_inp=="":
            self.updateStatusMessage("Error: Blank Data Slots") # Blank slots
        elif not capacity_inp.isdecimal():
            self.updateStatusMessage("Error: Capacity must be Integer") # Capacity Not Integer
        elif int(capacity_inp)<=0:
            self.updateStatusMessage("Error: Capacity must be Positive") # <=0
        else:
            self.updateStatusMessage("Status: Course Added") # Success
            ca = Course(CourseID=courseID_inp, CourseName=courseName_inp, NoStudents=int(capacity_inp), ProfName=prof_inp, RoomType=roomtype_inp)
            session.add(ca)                     
        self.updateTable()
        self.updateCourseList()
        ##REMOVE_THIS##session.commit()

    def previousPage(self):
        widget_menu.show()
        widget_course_add.hide()
        widget_course_add.updateStatusMessage("Click Remove Once To Pull Data")
        widget_course_remove.updateStatusMessage("Click Remove Once To Pull Data")


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

    widget_login = UI_form_login()
    widget_pick_timeslot = UI_form_pick_timeslot()
    widget_course_remove = UI_course_remove()
    widget_course_add = UI_course_add()
    #widget_menu = UI_form_main()
    #widget_menu_guest = UI_form_main_guest()

    widget_login.show()

    #widget_menu.show()
    
    sys.exit(app.exec_())

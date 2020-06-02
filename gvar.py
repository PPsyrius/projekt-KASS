# This Python file uses the following encoding: utf-8
# Global Variables are stored here

from sqliteDB import *

username_read = "Guest"
scheduleHeader = [ 'Location', 'Date', 'Time', 'ClassID', 'Class', 'Lecturer']
scheduleTableList = [
    ['','','','','','']
]
courseHeader = ['Course ID', 'Course Name', 'Class Capacity', 'Lecturer', 'Classroom Type']
courseTableList = [
    ['','','','','']
]
date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time = ['09:00-12:00', '13:00-16:00']
roomType = ['Lecture', 'ComLab']

profList = []
for p in session.query(Professor).order_by(Professor.ProfName):
    profList.append(p.ProfName)

courseList = []
for c in session.query(Course).order_by(Course.CourseID):
    profList.append(c.CourseID)

selectedCourseList = ["--Select Here--"]

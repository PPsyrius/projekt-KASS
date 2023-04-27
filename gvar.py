# Global Variables are stored here

from typing import Any, Dict

from sqliteDB import Course, Professor, Room, session

username_read = "Guest"

scheduleHeader = ["Location", "Date", "Time", "ClassID", "Class", "Lecturer"]
scheduleTableList = [["", "", "", "", "", ""]]
courseHeader = [
    "Course ID",
    "Course Name",
    "Class Capacity",
    "Lecturer",
    "Classroom Type",
]
courseTableList = [["", "", "", "", ""]]
profHeader = ["Lecturer ID", "Lecturer Name", "Email", "Password"]
profTableList = [["", "", "", ""]]
roomHeader = ["Room ID", "Room Capacity", "Classroom Type"]
roomTableList = [["", "", ""]]
date = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time = ["09:00-12:00", "13:00-16:00"]
roomType = ["Lecture", "ComLab"]

profList = []

for p in session.query(Professor).order_by(Professor.ProfName):
    profList.append(p.ProfName)
profIDList = []
for p in session.query(Professor).order_by(Professor.ProfID):
    profIDList.append(p.ProfID)
courseList = []
for c in session.query(Course).order_by(Course.CourseID):
    courseList.append(c.CourseID)
roomList = []
for r in session.query(Room).order_by(Room.RoomID):
    roomList.append(r.RoomID)

niceConflict = Dict[str, Any]
selectedCourseList = ["--Select Here--"]

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

sqlite3.connect("kass.db")

engine = create_engine('sqlite:///kass.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Admin(Base):
    __tablename__ = "admins"

    AdminID = Column(String, primary_key=True)
    AdminName = Column(String)
    Email = Column(String)
    Password = Column(String)

    def __repr__(self):
        return "Professor(AdminID = {}, AdminName = {}, Email = {}, Password = {})".format(self.AdminID, self.AdminName, self.Email, self.Password)


class Professor(Base):
    __tablename__ = "professors"

    ProfID = Column(String, primary_key=True)
    ProfName = Column(String)
    Email = Column(String)
    Password = Column(String)

    def __repr__(self):
        return "Professor(ProfID = {}, ProfName = {}, Email = {}, Password = {})".format(self.ProfID, self.ProfName, self.Email, self.Password)


class Room(Base):
    __tablename__ = "rooms"

    RoomID = Column(String, primary_key=True)
    RoomType = Column(String) # ComLab, Lecture
    Capacity = Column(Integer)

    def __repr__(self):
        return "Room(RoomID = {}, RoomType = {}, Capacity = {})".format(self.RoomID, self.RoomType, self.Capacity)


class RoomOccupancy(Base):
    __tablename__ = "roomOccupancies"

    RoomID = Column(String, primary_key=True)
    DateTime = Column(Integer, primary_key=True)
    CourseID = Column(String)

    def __repr__(self):
        return "RoomOccupancy(RoomID = {}, DateTime = {}, CourseID = {})".format(self.RoomID, self.DateTime, self.CourseID)


class Course(Base):
    __tablename__ = 'courses'

    CourseID = Column(String, primary_key=True)
    CourseName = Column(String)
    NoStudents = Column(Integer)
    ProfName = Column(String)
    RoomType = Column(String)  # ComLab, Lecture

    def __repr__(self):
        return "Course(CourseID = {}, CourseName = {}, NoStudents = {}, ProfName = {})".format(self.CourseID, self.CourseName, self.NoStudents, self.ProfName)


class CourseTimeSlot(Base):
    __tablename__ = "coursetimeslots"

    CourseID = Column(String, primary_key=True)
    DateTime = Column(Integer, primary_key=True)

    def __repr__(self):
        return "CourseTimeSlot(CourseID = {}, DateTime = {})".format(self.CourseID, self.DateTime)


Base.metadata.create_all(engine)

def generateRoomOccupancy():
    dateTimeList = [11, 12, 21, 22, 31, 32, 41, 42, 51, 52]
    for r in session.query(Room):
        for dt in dateTimeList:
            newRO = RoomOccupancy(RoomID=r.RoomID, DateTime=dt, CourseID=None)
            session.add(newRO)


r1 = Room(RoomID="IC01", RoomType="Lecture", Capacity=50)
r2 = Room(RoomID="IC02", RoomType="Lecture", Capacity=50)
r3 = Room(RoomID="IC03", RoomType="ComLab", Capacity=50)

session.add(r1)
session.add(r2)
session.add(r3)

generateRoomOccupancy()



courseToAdd = []

courseTStoAdd = []

c1 = Course(CourseID="1300", CourseName="Python", NoStudents=49, ProfName="Dr Visit", RoomType="Lecture")

cts1 = CourseTimeSlot(CourseID="1300", DateTime=12)
cts2 = CourseTimeSlot(CourseID="1300", DateTime=22)
cts3 = CourseTimeSlot(CourseID="1300", DateTime=32)

courseTStoAdd.append(cts1)
courseTStoAdd.append(cts2)
courseTStoAdd.append(cts3)

c2 = Course(CourseID="1301", CourseName="Python Lab", NoStudents=49, ProfName="Dr Visit", RoomType="ComLab")

cts4 = CourseTimeSlot(CourseID="1301", DateTime=42)
cts5 = CourseTimeSlot(CourseID="1301", DateTime=52)
cts6 = CourseTimeSlot(CourseID="1301", DateTime=11)

courseTStoAdd.append(cts4)
courseTStoAdd.append(cts5)
courseTStoAdd.append(cts6)

c3 = Course(CourseID="1302", CourseName="C", NoStudents=49, ProfName="Dr Ukrit", RoomType="Lecture")

cts7 = CourseTimeSlot(CourseID="1302", DateTime=31)
cts8 = CourseTimeSlot(CourseID="1302", DateTime=51)

courseTStoAdd.append(cts7)
courseTStoAdd.append(cts8)

c4 = Course(CourseID="1303", CourseName="C Lab", NoStudents=49, ProfName="Dr Ukrit", RoomType="ComLab")

cts9 = CourseTimeSlot(CourseID="1303", DateTime=42)
cts10 = CourseTimeSlot(CourseID="1303", DateTime=41)

courseTStoAdd.append(cts9)
courseTStoAdd.append(cts10)

c5 = Course(CourseID="1304", CourseName="Logic", NoStudents=30, ProfName="Dr Natthapong", RoomType="Lecture")

cts11 = CourseTimeSlot(CourseID="1304", DateTime=12)
cts12 = CourseTimeSlot(CourseID="1304", DateTime=32)

courseTStoAdd.append(cts11)
courseTStoAdd.append(cts12)

c6 = Course(CourseID="1305", CourseName="Electricity", NoStudents=47, ProfName="Dr Michael", RoomType="Lecture")

cts13 = CourseTimeSlot(CourseID="1305", DateTime=52)
cts14 = CourseTimeSlot(CourseID="1305", DateTime=51)

courseTStoAdd.append(cts13)
courseTStoAdd.append(cts14)



courseToAdd.append(c1)
courseToAdd.append(c2)
courseToAdd.append(c3)
courseToAdd.append(c4)
courseToAdd.append(c5)
courseToAdd.append(c6)

session.add_all(courseToAdd)


session.add_all(courseTStoAdd)

session.commit()

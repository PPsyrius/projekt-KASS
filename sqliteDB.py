from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
    DateTime = Column(Integer)
    CourseID = Column(String)

    def __repr__(self):
        return "RoomOccupancy(RoomID = {}, DateTime = {}, CourseID = {})".format(self.RoomID, self.DateTime, self.CourseID)


class Course(Base):
    __tablename__ = 'courses'

    CourseID = Column(String, primary_key=True)
    CourseName = Column(String)
    NoStudents = Column(Integer)
    ProfName = Column(String)
    RoomType = Column(String) # ComLab, Lecture

    def __repr__(self):
        return "Course(CourseID = {}, CourseName = {}, NoStudents = {}, ProfName = {})".format(self.CourseID, self.CourseName, self.NoStudents, self.ProfName)


class CourseTimeSlot(Base):
    __tablename__ = "coursetimeslots"

    CourseID = Column(String)
    DateTime = Column(Integer)

    def __repr__(self):
        return "CourseTimeSlot(CourseID = {}, DateTime = {})".format(self.CourseID, self.DateTime)


Base.metadata.create_all(engine)

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import sqlite3
conn = sqlite3.connect('kass.db')

engine = create_engine('sqlite:///kass.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Professor(Base):
    __tablename__ = "professors"

    profid = Column(String, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "Professor(profid = {}, fullname = {}, email = {}, password = {})".format(self.profid, self.fullname, self.email, self.password)


class Course(Base):
    __tablename__ = 'courses'

    courseid = Column(String, primary_key=True)
    name = Column(String)
    no_students = Column(Integer)
    date = Column(Integer)  # Monday = 1 ... Friday = 5
    time = Column(Integer)  # 1 for Morning, 2 for Afternoon
    profname = Column(String)

    def __repr__(self):
        return "Course(courseid = {}, name = {}, no_students = {}, date = {}, time = {}, profname = {})".format(self.courseid, self.name, self.no_students, self.date, self.time, self.profname)

Base.metadata.create_all(engine)

"""
pof = Professor(profid="4819", fullname="Teevisit Kolpak", email="teevisitk@kmitl.ac.th", password="abcdefg")

print(pof.fullname)

session.add(pof)

q1 = session.query(Professor).filter_by(profid='4819').first()

print(q1)

pof.fullname='Texas Valens'

print(session.dirty)
"""
# Profs
prof1 = Professor(profid="1060", fullname="Dr Visit", email="visit@kmitl.ac.th", password="kmitlvi1060")
prof2 = Professor(profid="1061", fullname="Dr Ukrit", email="ukrit@kmitl.ac.th", password="kmitluk1061")
prof3 = Professor(profid="1062", fullname="Dr Tui", email="ajtui@kmitl.ac.th", password="kmitltu1062")
prof4 = Professor(profid="1063", fullname="Aj Michael", email="michael@kmitl.ac.th", password="kmitlmi1063")
prof5 = Professor(profid="1064", fullname="Dr Natthapong", email="natthapong@kmitl.ac.th", password="kmitlna1064")
prof6 = Professor(profid="1065", fullname="Dr Philosophy", email="philo@kmitl.ac.th", password="kmitlph1065")
prof7 = Professor(profid="1066", fullname="Dr Surin", email="surin@kmitl.ac.th", password="kmitlsu1066")
prof8 = Professor(profid="1067", fullname="Dr Chaiwat", email="chaiwat@kmitl.ac.th", password="kmitlch1067")
prof9 = Professor(profid="1068", fullname="Dr Veera", email="veera@kmitl.ac.th", password="kmitlve1068")
prof10 = Professor(profid="1069", fullname="Dr Academiceng", email="acaeng@kmitl.ac.th", password="kmitlac1069")
proflist = [prof1, prof2, prof3, prof4, prof5, prof6, prof7, prof8, prof9, prof10]

session.add_all(proflist)

# Courses
course1y1 = Course(courseid="1300", name="Introduction to Programming with Python", no_students=50, date=1, time=2, profname="Dr Visit")
course10y1 = Course(courseid="1301", name="Introduction to Programming with Python Lab", no_students=50, date=2, time=2, profname="Dr Visit")
course2y1 = Course(courseid="1302", name="C Programming", no_students=50, date=1, time=1, profname="Dr Ukrit")
course9y1 = Course(courseid="1303", name="C Programming Lab", no_students=50, date=5, time=2, profname="Dr Ukrit")
course3y1 = Course(courseid="1304", name="Calculus 1", no_students=50, date=2, time=1, profname="Dr Tui")
course4y1 = Course(courseid="1305", name="Introduction to Logic", no_students=50, date=4, time=1, profname="Dr Natthapong")
course5y1 = Course(courseid="1306", name="Basic Electricity", no_students=50, date=3, time=2, profname="Aj Michael")
course8y1 = Course(courseid="1307", name="Basic Electricity Lab", no_students=50, date=4, time=2, profname="Aj Michael")
course6y1 = Course(courseid="1308", name="Academic English 1", no_students=25, date=3, time=1, profname="Dr Academiceng")

course1y2 = Course(courseid="1309", name="Linear Algebra", no_students=50, date=2, time=2, profname="Dr Chaiwat")
course2y2 = Course(courseid="1310", name="Advanced Object Oriented Programming", no_students=50, date=4, time=1, profname="Dr Veera")
course7y2 = Course(courseid="1311", name="Advanced Object Oriented Programming Lab", no_students=50, date=4, time=2, profname="Dr Veera")
course3y2 = Course(courseid="1312", name="Computer Organization and Assembly Language", no_students=50, date=3, time=1, profname="Dr Surin")
course4y2 = Course(courseid="1313", name="Computer Organization and Assembly Language Lab", no_students=50, date=2, time=1, profname="Dr Surin")
course5y2 = Course(courseid="1314", name="Data Structure and Algorithms", no_students=50, date=5, time=2, profname="Dr Natthapong")
course6y2 = Course(courseid="1315", name="Data Structure and Algorithms Lab", no_students=50, date=1, time=2, profname="Dr Natthapong")
courselist = [course1y1, course10y1, course2y1, course9y1, course3y1, course4y1, course5y1, course8y1, course6y1,
                course1y2, course2y2, course7y2, course3y2, course4y2, course5y2, course6y2]

session.add_all(courselist)

session.commit()


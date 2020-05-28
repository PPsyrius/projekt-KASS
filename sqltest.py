from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
    date = Column(Integer)  # Monday = 1 ... Friday = 6
    time = Column(Integer)  # 1 for Morning, 2 for Afternoon


Base.metadata.create_all(engine)

pof = Professor(profid="4819", fullname="Teevisit Kolpak", email="teevisitk@kmitl.ac.th", password="abcdefg")

print(pof.fullname)

session.add(pof)

q1 = session.query(Professor).filter_by(profid='4819').first()

print(q1)

pof.fullname='Texas Valens'

print(session.dirty)


from sqliteDB import *

def readyToGenerate():      # Check if every course has at least one CourseTimeSlot
    cIDcheck = []

    for c in session.query(Course).order_by(Course.CourseID):
        cIDcheck.append(c.CourseID)

    for cts in session.query(CourseTimeSlot).order_by(CourseTimeSlot.CourseID):
        if cts.CourseID in cIDcheck:
            cIDcheck.remove(cts.CourseID)

    if not cIDcheck:
        return True
    else:
        return False



courseTimeSlot = {}
courseAvail = {}

conflictTable = []

for c in session.query(Course):

    freeList = []            # INPUT FROM CourseTimeSlot
    slots = 0
    #print(c.CourseID)
    for cts in session.query(CourseTimeSlot).filter_by(CourseID=c.CourseID):
        #print(cts)
        freeList.append(cts.DateTime)
        slots += 1

    courseTimeSlot[c.CourseID] = slots

    courseAvail[c.CourseID] = freeList

print(courseTimeSlot)
print(courseAvail)



freeRoomDict = {}   #INPUT FROM RoomOccupancy

for r in session.query(Room):
    listRO = []
    for ro in session.query(RoomOccupancy).filter_by(RoomID=r.RoomID):
        listRO.append(ro.DateTime)
    freeRoomDict[r.RoomID] = listRO

#print(freeRoomDict)


for k, v in freeRoomDict.items():
    room = session.query(Room).filter_by(RoomID=k).first()
    rType = room.RoomType

    newRO = v.copy()
    for j in v:

        lowestTimeSlotCourse = [None, 999]
        coursesInThisTime = []

        for x, y in courseAvail.items():
            course = session.query(Course).filter_by(CourseID=x).first()
            if j in y and rType == course.RoomType:
                coursesInThisTime.append(x)
                if courseTimeSlot[x] < lowestTimeSlotCourse[1]:
                    lowestTimeSlotCourse[0] = x
                    lowestTimeSlotCourse[1] = courseTimeSlot[x]


        #print(lowestTimeSlotCourse)
        if lowestTimeSlotCourse[0] != None:
            #print("Deleting ", lowestTimeSlotCourse[0])
            coursesInThisTime.remove(lowestTimeSlotCourse[0])
            #print("Adding", lowestTimeSlotCourse[0], "to", i, j, freeRoom[i][j])
            newRO[newRO.index(j)] = lowestTimeSlotCourse[0]

            courseAvail.pop(lowestTimeSlotCourse[0])

        #print(i, freeRoom[i][j], coursesInThisTime)
        for x in coursesInThisTime:
            courseTimeSlot[x] -= 1

    #print(k, newRO)

    freeRoomDict[k] = newRO

for k in courseAvail.keys():
    conflictTable.append(k)

def NiceTimeTable():             # Use this to output the Nicely formatted time table
    GeneratedTimeTable = []
    schedule = [11, 12, 21, 22, 31, 32, 41, 42, 51, 52]
    date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time = ["09:00-12:00", "13:00-16:00"]

    for k, v in freeRoomDict.items():
        print(k , v)
        for j in v:
            if isinstance(j, str):
                c = session.query(Course).filter_by(CourseID=j).first()

                d = schedule[v.index(j)] // 10 - 1
                t = schedule[v.index(j)] % 10 - 1
                newTimeTable = [k, date[d], time[t], j, c.CourseName, c.ProfName]
                GeneratedTimeTable.append(newTimeTable)

    print(GeneratedTimeTable)
    return GeneratedTimeTable

conflictTable.append('1300')
conflictTable.append('1302')

def NiceConflict():         # Use this to output a dict of professors with the conflicting classes
    courses = session.query(Course)
    ConflictDict = {}
    conflictCourseList = []

    print("Conflicting courses:", conflictTable)

    for co in courses:
        if co.CourseID in conflictTable:
            conflictCourseList.append("{} - {}".format(co.CourseID, co.CourseName))
            ConflictDict[co.ProfName] = conflictCourseList
    print(ConflictDict)

NiceConflict()

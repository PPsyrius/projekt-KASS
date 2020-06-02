from sqliteDB import *

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
    newRO = v.copy()
    for j in v:


        lowestTimeSlotCourse = [None, 999]
        coursesInThisTime = []

        for x, y in courseAvail.items():
            if j in y:
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

for k, v in freeRoomDict.items():
    print(k , v)

print("Conflict courses:", conflictTable)



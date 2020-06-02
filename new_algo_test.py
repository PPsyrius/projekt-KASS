# This Python file uses the following encoding: utf-8

import random

courseDict = {}
courseAvail = {}

conflictTable = []

schedule = [11, 12, 21, 22, 31, 32, 41, 42, 51, 52]

for i in range(1000, 1030):  # INPUT FROM COURSE TABLE (COURSEID)

    freeList = []            # INPUT FROM CourseTimeSlot
    freeSlots = random.randint(1, 5)

    courseDict[str(i)] = freeSlots

    for j in range(freeSlots):
        time = schedule[random.randint(0, 9)]
        if time not in freeList:
            freeList.append(time)

    courseAvail[str(i)] = freeList

#print(courseDict)
#print(courseAvail)


freeRoom = [[11, 12, 21, 22, 31, 32, 41, 42, 51, 52],
            [11, 12, 21, 22, 31, 32, 41, 42, 51, 52],
            [11, 12, 21, 22, 31, 32, 41, 42, 51, 52]]   #INPUT FROM RoomOccupancy

for i in range(len(freeRoom)):

    for j in range(len(freeRoom[0])):
        lowestTimeSlotCourse = ["Null", 999]
        coursesInThisTime = []

        for k, v in courseAvail.items():
            if freeRoom[i][j] in v:
                coursesInThisTime.append(k)
                if courseDict[k] < lowestTimeSlotCourse[1]:
                    lowestTimeSlotCourse[0] = k
                    lowestTimeSlotCourse[1] = courseDict[k]
                #print("{} has {} timeslots".format(k, courseDict[k]))

        #print(lowestTimeSlotCourse)
        if lowestTimeSlotCourse[0] != "Null":
            #print("Deleting ", lowestTimeSlotCourse[0])
            coursesInThisTime.remove(lowestTimeSlotCourse[0])
            #print("Adding", lowestTimeSlotCourse[0], "to", i, j, freeRoom[i][j])
            freeRoom[i][j] = lowestTimeSlotCourse[0]

            courseAvail.pop(lowestTimeSlotCourse[0])

        #print(i, freeRoom[i][j], coursesInThisTime)
        for x in coursesInThisTime:
            courseDict[x] -= 1

for k in courseAvail.keys():
    conflictTable.append(k)

for r in range(len(freeRoom)):
    print("Room", r, ":", freeRoom[r])

print("Conflict courses:", conflictTable)

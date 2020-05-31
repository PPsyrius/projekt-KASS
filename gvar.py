# This Python file uses the following encoding: utf-8
# Global Variables are stored here

username_read = "Guest"
scheduleHeader = ['Period', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
scheduleTableList = [
    []
]
courseHeader = ['Course ID', 'Course Name', 'Class Capacity', 'Date', 'Period', 'Professor']
courseTableList = [
    []
]
date = ["Mon", "Tue", "Wed", "Thu", "Fri"]
time = ["09:00-12:00", "13:00-16:00"]


from sqliteDB import *

rooms = 5
course_name = [None for _ in range(rooms*len(date)*len(time))]
course_id = [None for _ in range(rooms*len(date)*len(time))]
prof_name = [None for _ in range(rooms*len(date)*len(time))]
date_lst = [None for _ in range(rooms*len(date)*len(time))]
time_lst = [None for _ in range(rooms*len(date)*len(time))]
display_lst = [None for _ in range(rooms*len(date)*len(time))]
stud_lst = [None for _ in range(rooms*len(date)*len(time))]

i = 0
for c in session.query(Course).order_by(Course.time).order_by(Course.date):
    course_name[i] = c.name
    course_id[i] = c.courseid
    prof_name[i] = c.profname
    date_lst[i] = c.date
    time_lst[i] = c.time
    stud_lst[i] = c.no_students
    i += 1

print("\n\n\n")

room_name = []
for room in range(rooms):
    if (room+1) % 10 == 0: room_name.append("IC" + str(room+1))
    else: room_name.append("IC0" + str(room+1))

for t in range(len(time_lst)):
    if time_lst[t] == 1: time_lst[t] = time[0]
    elif time_lst[t] == 2: time_lst[t] = time[1]
    
for d in range(len(date_lst)):
    if date_lst[d] == 1: date_lst[d] = date[0]
    elif date_lst[d] == 2: date_lst[d] = date[1]
    elif date_lst[d] == 3: date_lst[d] = date[2]
    elif date_lst[d] == 4: date_lst[d] = date[3]
    elif date_lst[d] == 5: date_lst[d] = date[4]

for s in range(len(stud_lst)):
    if stud_lst[s] is not None:
        if stud_lst[s] >= 25: stud_lst[s] = "Lecture 50"
        elif stud_lst[s] < 25: stud_lst[s] = "Lecture 25"
        else: stud_lst[s] = "Exceed"

for i in range(len(stud_lst)):
    if course_name[i] is not None:
        if course_name[i][-3:] == "Lab":
            stud_lst[i] = "Lab"

for l in range(len(display_lst)):
    if time_lst[l] != None:
        display_lst[l] = date_lst[l] + "\t" + time_lst[l] + "\t" + course_name[l] + "\t" + course_id[l] + "\t" + prof_name[l] + "\t" + stud_lst[l]

for i in display_lst:
    print(i)

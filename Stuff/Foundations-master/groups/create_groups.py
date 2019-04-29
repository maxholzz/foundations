
import csv 
import random
import math 

# list of all the students' email addresses
student_list = []

# read initial file, save names to dict. 
with open("emails.csv") as f:
    r = csv.reader(f)
    for row in r: 
        student_list.append(row[0])

f.close()

number_groups = 9
number_participants = 4
number_weeks = 3 
weeks_groups = {} # mega dictionary. 

# dict containing 0-2 as keys, representing weeks.
# Each value is itself a dict, which has 0-8 as keys, representing week, and a list of student email addresses.
for week in range(number_weeks):
    weeks_groups[week]={} # a given week's groups 
    for g in range(number_groups): 
        weeks_groups[week][g] = [] # a given group's students in a given week. 

# loop over all the weeks 
for week in range(number_weeks):
    # keep looping until all students are in a group for the first week. 
    this_week_list = student_list.copy()
    while len(this_week_list) > 0:
        # select students at random from list.
        this_student = random.choice(this_week_list)
        this_week_list.remove(this_student)

        ## decide which group: number of seats taken divided by the size a group, rounded down. 
        # this will give you the next available group, as an int. 
        spots_taken = len(student_list) - len(this_week_list)
        group = math.floor(spots_taken/number_participants)
        
        # normal case for number_groups * number_particpants 
        if (spots_taken < number_groups*number_participants):
            weeks_groups[week][group].append(this_student)

        # for "overflow" cases, add to a group which has number_participants already. not very robust.
        else: 
            for g in range(number_groups):
                if len(weeks_groups[week][g]) <= number_participants:
                    weeks_groups[week][g].append(this_student)
                    break

    #print(weeks_groups[week])

# output group view to text, useful for a quick overview of who should be there. 
with open("groups.txt","w+") as f:
    for week in range(number_weeks):
        f.write("\nWeek {week}\n".format(week=week))
        for group,students in weeks_groups[week].items():
            f.write("Group: {group}, Students: {students}\n".format(
                group=group, students=students))
f.close()

f_csv = open("students.csv","w+")
f_txt = open("students.txt", "w+")
# output student view, useful for student & spreadhseet. 
for student in student_list:
    csv_string = "{student},".format(student=student) # string for final output to csv 
    for week in range(number_weeks):
        for group, students in weeks_groups[week].items():
            if student in students:
                    # human readable output, checking how many string methdos I can stuff in at once. 
                    f_txt.write("{student} Week: {week} Group: {group}\n".format(student=" ".join(student[:-12].split(".")).title(), week=week, group=group))
                    # machine readable output
                    csv_string += "{group},".format(group=str(group))
    f_csv.write(csv_string[:-1] + "\n")

f_csv.close()
f_txt.close()

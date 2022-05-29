
courses_and_avg = {}

stop = int(input("another? 0 to stop "))
while stop!= 0:
    course_name = input("Enter the course name: ")
    grade = input("Enter Grade: ")
    weight = input("Enter weight: ")
    courses_and_avg[course_name] = {"Grade": grade, "weight": weight}
    stop = int(input("another? 0 to stop "))


tot_weight = 0
tot_weighted_grades = 0

for course in courses_and_avg:

    
    tot_weight += int(courses_and_avg[course]["weight"])
    tot_weighted_grades += (int(courses_and_avg[course]["weight"]) * int(courses_and_avg[course]["Grade"]))
weighted_avg = tot_weighted_grades / tot_weight

print("The weighted average of your grades is: \n", weighted_avg)

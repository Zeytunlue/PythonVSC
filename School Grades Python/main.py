#Student's name
student_name = "Sam"
#Student's grades
math_grade = 88
science_grade = 75
english_grade = 90
geology_grade = 69
#Calculating the total grade
total_grade = math_grade + science_grade + english_grade +geology_grade
max_grade = 400
#Calculating the percentage value 
total_percentage = total_grade / max_grade * 100
print(f"Sam's total percentage is {total_percentage}%")
total_percentage = int(total_percentage)
sport_grade = 0
#Did he pass?
did_student_pass = total_percentage > 50
sporting_activities = bool(sport_grade)
#Printing the results
print(f"Sam participated in sporting activities: {sporting_activities}")
print(f"Sam's total percentage as an integer is {total_percentage}%")
print(f"Sam passed to the next semester: {did_student_pass}")
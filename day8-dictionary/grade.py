student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇

for key, value in student_scores.items():
    #print(key, value)
    if value >= 91:
        std_grade = "Outstanding"
    elif value >= 81:
        std_grade = "Exceeds Expectations"
    elif value >= 71:
        std_grade = "Acceptable"
    else:
        std_grade = "Fail"
    student_grades[key] = std_grade
    print(key, student_grades[key])


# 🚨 Don't change the code below 👇

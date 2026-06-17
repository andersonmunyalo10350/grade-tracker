# Grade Tracker Version 1.0
grades = [80, 90, 70, 85]

def calculate_average(grade_list):
    total = sum(grade_list)
    return total / len(grade_list)

print("Average Grade:", calculate_average(grades))

# Grade Tracker Version 1.1
grades = [80, 90, 70, 85]

def calculate_average(grade_list):
    total = sum(grade_list)
    return total / len(grade_list)

# NEW FEATURE: Assign Letter Grade
avg = calculate_average(grades)
if avg >= 80:
    letter = 'a'
else:
    letter = 'B'

print("Average Grade:", avg)
print("Final Letter Grade:", letter)

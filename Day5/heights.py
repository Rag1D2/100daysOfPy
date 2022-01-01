# Given a list of student_heights, find the average
# Cannot use len and sum
student_heights = [156, 178, 165, 171, 187]

total_height = 0
for height in student_heights:
    total_height += height

# print(total_height)

total_students = 0
for student in student_heights:
    total_students += 1
# print(total_students)

average_height = round(total_height / total_students)

print(average_height)

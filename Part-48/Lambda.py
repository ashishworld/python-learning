students = [
    ("ashish", 92),
    ("nakul", 97),
    ("nandhini", 60),
    ("chhaya", 72)
]


# def sort_students(stu):
#     return stu[1]


# students.sort(key=sort_students, reverse=True)
# students.sort(key=lambda parameter:statement)
students.sort(key=lambda stu: stu[1])
print(students)

students = [
    ("ashish", 92),
    ("nakul", 97),
    ("nandhini", 60),
    ("chhaya", 72)
]
# new_list = []
# for x in students:
#     if x[1] > 90:
#         new_list.append(x)

# or

new_list = filter(lambda x: x[1] > 90, students)
new_list = list(new_list)
print(new_list)

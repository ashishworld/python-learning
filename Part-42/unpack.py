# names = ['ashish', "lalchandra", "tiwari"]

# first = names[0]
# second = names[1]
# third = names[2]
# print(first)
# print(second)
# print(third)

# or
# first, second, third = names
# print(first)
# print(second)
# print(third)

# or to avoid other names to unpack
# first, second, = names[0:2]
# print(first)
# print(second)
# print(third)

# or
names = ["ashish", "lalchandra", "tiwari", 1, 2, 3, 4, "nakul", "nandini"]
first, second, third, *list2, fourth, fifth = names
print(first)
print(second)
print(third)
print(fourth)
print(list2)
print(fifth)

# def add(num1, num2):
#     result = num1+num2
#     print(result)


# add(2, 3)

# ##############


# def add_3(num1, num2, num3):
#     result = num1+num2+num3
#     print(result)


# add_3(2, 3, 5)
############


def add(*num):
    result = 0
    for n in num:
        result = result + n
    print(result)


add(2, 3, 5, 9, 80)

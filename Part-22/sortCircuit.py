# logical AND: True if the both the operands are true x and y
# logical OR: True if either of the operands is true x or y
# logical NOT: True if operand is false not x

ssc = 60
hsc = 65
test = 45

if ssc >= 60 and hsc >= 60 and test >= 60:
    print("Eligible")
else:
    print("Not Eligible")

ssc = 50
hsc = 65
test = 85

if ssc >= 60 or hsc >= 60 or test >= 60:
    print("Eligible")
else:
    print("Not Eligible")

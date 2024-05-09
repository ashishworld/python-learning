print("Legal age of marrige in India")
gender = input("Enter Male (m) or Female (f):")
age = int(input("Enter age: "))

if gender == "m":
    if age >= 21:
        print("Legal age of marriage")
    else:
        print("child marriage")

elif gender == "f":
    if age >= 18:
        print("Legal age of marriage")
    else:
        print("child marriage")

else:
    print("Enter for male and f for female")

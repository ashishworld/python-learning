def add_student(**args):
    for x, y in args.items():
        print(f"{x} = {y}")


add_student(name="ashish", roll=1, age=27)

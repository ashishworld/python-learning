# def hello():
#     message = "good morning!"
#     print(message)


# hello()

# Global Variable
var0 = "Global Var"


def fun1():
    global var0
    var0 = "local var"
    print(var0)


fun1()
print(var0)

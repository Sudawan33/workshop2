x = "awesome"


def mafunc():
    global x
    print("python is " + x)
    x = "fantastic"


myfunc()
print("python is " + x)
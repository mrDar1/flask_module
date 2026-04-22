def outer():
    def inner():
        print("Inner")
    return inner


f = outer()
f()

def dar_decorator(func):
    def wrapper():
        print("🔵 before function")
        func()
        print("🔴 after function")
    return wrapper

# ! must uncomment 1st or 2nd option!


# 1st alternative:
# def say_hello():
#     print("Hello")


# say_hello = dar_decorator(say_hello)
# say_hello()
# 1st alternative - end.


# 2nd alternative - do the same - shorter with @:
@dar_decorator
def say_hello():
    print("Hello")


say_hello()
# 2nd alternative - do the same - shorter with @ - end.

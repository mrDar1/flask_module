def dar_decorator(func):
    def wrapper():
        print("🔵 before function")
        func()
        print("🔴 after function")
    return wrapper

# ! must uncomment 1st or 2nd option!


# 1st alternative:
def say_name(name):
    print(name)


say_name("Yuval")

# * note how option 2 failed - since the decorator dont let us work with args.
# output:
# TypeError: dar_decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given


# 2nd alternative:
# @dar_decorator
# def say_name(name):
#     print(name)


# say_name("Yuval")

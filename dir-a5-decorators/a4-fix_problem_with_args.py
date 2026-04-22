def dar_decorator(func):
    def wrapper(*args, **kwargs):
        print("beofre")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper


@dar_decorator
def say_name(name):
    print(name)


say_name("Yuval")

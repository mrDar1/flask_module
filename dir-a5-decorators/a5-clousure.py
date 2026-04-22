def outer(x):
    def inner(y):      # inner "closes over" x
        return x + y
    return inner


add5 = outer(5)
print(add5(3))  # 8  — x=5 is remembered

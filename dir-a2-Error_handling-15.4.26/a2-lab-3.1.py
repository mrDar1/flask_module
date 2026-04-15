def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("[Error] number cannot be negative")
        return age
    except ValueError as e:
        print(f"Error {e}")


age = get_age()
print("Your age is:", age)

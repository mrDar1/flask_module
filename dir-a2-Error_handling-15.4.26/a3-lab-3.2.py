users = ["Alice", "Bob", "Charlie"]

def get_user(index):
    return users[index]


user_index = input("Enter user index: ")
user = get_user(int(user_index))

print("Selected user:", user)
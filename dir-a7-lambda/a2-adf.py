# 1 - multiply each element:
nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
print(result)

# 2 - filter:
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 3 - sorted:
people = [
    {"name": "A", "age": 30},
    {"name": "B", "age": 20}
]

sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)


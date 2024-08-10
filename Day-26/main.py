numbers = [1,2,3]

new_list = [number + 1 for number in numbers]
print(new_list)

new_list = [number * 2 for number in range(1, 5)]
print(new_list)


# Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Firaol", "Dave", "Eleanor", "Freda"]

short_Names = [name for name in names if len(name) < 5]
print(short_Names)
upper_Names = [name.upper() for name in names if len(name) > 4]
print(upper_Names)
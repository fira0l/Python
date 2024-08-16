## FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["sddfds"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_msg:
#     print(f"the key {error_msg} Does not exist!!!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error i made")




## KeyError

# a_dictionary = {"key":"value"}
# value = a_dicitonary["non_existent_key"]

## IndexError

# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

## TypeError

# text = "abc"
# print(text + 5)

"""
try: Something that might cause an exception
except: do this if there was an exception
else: do this if there were no exceptions
finally: Do this no matter what happens
"""


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError(f"The f u mean ur height is {height}: stop dreaming")

bmi = weight/ height ** 2
print(bmi)




fruits = ["Apple", "pear", "Orange"]


def make_pi(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pi(6)

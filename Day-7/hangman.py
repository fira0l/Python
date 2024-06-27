import random

word_list =["ardvark","baboon","camel"]

choosen_word = ""

# letter = input("guess a letter : ")

chosen_word = random.choice(word_list)
print(f"Psst, The choosen Word is {chosen_word}.")

guess = input("Insert a letter to guess: ").lower()

for i in chosen_word:
    if i == guess:
        choosen_word += i
    else:
        choosen_word += " _ "
choosen_word.split()
print(choosen_word)
#     if i != guess:
#         choosen_word.insert(i.index(i),"_")
#     else:
#         choosen_word.insert(i.index(i),i)
# print(choosen_word)

# for char in chosen_word:
#     if (guess == char):
#         print(f"{char}",end=" ")
#     else:
#         print("_",end=" ")
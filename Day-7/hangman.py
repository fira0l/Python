import random

word_list =["ardvark","baboon","camel"]

display= []
counter = 0

# letter = input("guess a letter : ")

chosen_word = random.choice(word_list)
print(f"Psst, The choosen Word is {chosen_word}.")

for letter in chosen_word:
    display += "_"
print(display)


while ("_" in display):
    guess = input("Guess a Letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
print("You win!!!")
    
    

    
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
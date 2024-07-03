import random
import hangman_Arts as arts
import hangman_words as words

print(arts.logo)


word_list =words.word_list

lives = 6 
end_of_game = False

display= []
counter = 0

# letter = input("guess a letter : ")

chosen_word = random.choice(word_list)
# print(f"Psst, The choosen Word is {chosen_word}.")

for letter in chosen_word:
    display += "_"
print(display)


while not end_of_game:
    guess = input("Guess a Letter: ").lower()
    
    if guess in display:
        print(f"You Have already guessed {guess} letter")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        print(f"You Guessed {guess},that is not in the Word, You lose a life ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            
    
    if "_" not in display:
        end_of_game = True
        print("You Win.")
        
    print(arts.stages[lives])

    
    

    
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
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
end_of_cipher = False
while not end_of_cipher:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # cont = input("Do you want to Continue: \"Yes\" or \"no\"")
  
  shift = shift % 26
  
  def ceaser(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_amount *=-1
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char
    print(f"The {cipher_direction}d text is:' {end_text} '")
  ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
  cont = input("Do you want to Continue: \"Yes\" or \"no\"").lower()
  if cont == "no":
    end_of_cipher = True
    print("Good Bye") 
  
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
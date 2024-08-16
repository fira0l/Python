# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_data_dict)

# for (index,row) in


def generate_phonetic():
    user_input = input("Enter a Word: ")
    try:
        nato_phonetic_converted = [nato_data_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, ONly letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_phonetic_converted)

generate_phonetic()
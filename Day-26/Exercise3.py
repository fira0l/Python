with open("file1.txt") as fileone:
    file1_data = fileone.readlines()
    # numbers_in_fileone = [number for number in fileone.readlines()]
    # cleaned_number = []
    # for number in numbers_in_fileone:
    #     number = number.strip()
    #     cleaned_number.append(int(number))

with open("file2.txt") as filetwo:
    file2_data = filetwo.readlines()

    # numbers_in_filetwo = [number for number in filetwo.readlines()]
    # cleaned_number_in_two = []
    # for number in numbers_in_filetwo:
    #     number = number.strip()
    #     cleaned_number_in_two.append(int(number))
    #

result = [int(num) for num in file1_data if num in file2_data]
print(result)
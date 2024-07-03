row1 = ['🪟','🪟','🪟']
row2 = ['🪟','🪟','🪟']
row3 = ['🪟','🪟','🪟']

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to Put the treasure? ")

column = int(position[0])
row = int(position[1])

colIndex = column-1
rowIndex = row -1

if (rowIndex == 0):
    row1[colIndex] = "X"
elif(rowIndex == 1):
    row2[colIndex] = "X"
elif(rowIndex == 2):
    row3[colIndex] = "X"
else:
    print("Wrong ROW NUMBER")

print(f"{row1}\n{row2}\n{row3}")



# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[0]) 

banner = """
#     #                                                                  
#  #  # #    #  ####     #  ####     #####    ##   #   # # #    #  ####  
#  #  # #    # #    #    # #         #    #  #  #   # #  # ##   # #    # 
#  #  # ###### #    #    #  ####     #    # #    #   #   # # #  # #      
#  #  # #    # #    #    #      #    #####  ######   #   # #  # # #  ### 
#  #  # #    # #    #    # #    #    #      #    #   #   # #   ## #    # 
 ## ##  #    #  ####     #  ####     #      #    #   #   # #    #  ####  
"""
print(banner)

import random

names_string = input("Give me everybody's names, separated by comma. like ', '")
names = names_string.split(', ')
print(names)

indexs_len = len(names)-1

choosen = names[random.randint(0,indexs_len)]

print(f"{choosen} is going to buy the meal Today!")

programming_dictionary = {
    "bug":"An error in a program that prevents the program from running as excpected",
    "function":"A piece of code that you can easily call over and over again",
    "loop":"The action of doing sommething over and over again"
}



print(programming_dictionary)

#Nesting Starts ffrom here 

capitals = {
    "France":"Paris",
    "Germeny":"Berlin"
}

#Nesting Lists inside a dictionary 

travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Gremany":{"cities_visited":["Berlin","Hamburg","Stuttgrat"],"total_visits":5}
}

#Nesting Dictionaries insde lists 

travel_log = [
    {
        "Country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12},
    {
        "Country":"Gremany",
        "cities_visited":["Berlin","Hamburg","Stuttgrat"],
        "total_visits":5}
]

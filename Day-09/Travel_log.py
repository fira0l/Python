travel_log = [
    {
        "Country":"France",
        "cities":["Paris","Lille","Dijon"],
        "total_visits":12},
    {
        "Country":"Gremany",
        "cities":["Berlin","Hamburg","Stuttgrat"],
        "total_visits":5}
]


def add_new_country(name,travel_time,capitals):
    travel_log.append({
        "Country":name,
        "cities":capitals,
        "total_visits":travel_time
    })
    
    print(f"You Have Visited {name} {travel_time}.")
    print(f"You Have been to {capitals[0]} and {capitals[1]} .")
    

add_new_country("Russia",2,["Moscow","Saint Petersburg",""])
print(travel_log)
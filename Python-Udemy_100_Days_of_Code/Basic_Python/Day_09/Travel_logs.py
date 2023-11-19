country = input('Country name\n') #Country Name
visits = int(input('Number time visted\n')) #Number Of Visits
list_of_cities = eval(input('City name\n')) #Create list from formatted

travel_log =[
    {
        "country":'France',
        "total_vists":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":'Germany',
        "total_vists":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]


def add_new_country(country,visits,list_of_cities):
    new_entry={}

    new_entry["country"] = country
    new_entry["total_vists"] = visits
    new_entry["cities"] = list_of_cities
    travel_log.append(new_entry)

    print(travel_log)

add_new_country(country,visits,list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['total_vists']}.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")
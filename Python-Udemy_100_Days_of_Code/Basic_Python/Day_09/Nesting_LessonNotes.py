travel_log = {
    "France" :{"citied_visited":["Paris","Lille","Dijon"],"total_vists":12},
    "Germany":{"citied_visited":["Berlin","Hamburg","Stuttgart"],"total_vists":5},
}

# print(travel_log['France']['total_vists'])

# Nesting Dictionary in a list

travel_log =[
    {
        "country":'France',
        "citied_visited":["Paris","Lille","Dijon"],
        "total_vists":12
    },
    {
        "country":'Germany',
        "citied_visited":["Berlin","Hamburg","Stuttgart"],
        "total_vists":5
    },
]


# print(travel_log.sort())

# print(travel_log[1].items())

high = 0
keep = []
for i in range(len(travel_log)):
    # print (i, travel_log[i]['total_vists'])

    if travel_log[i]['total_vists'] > high:
        high = travel_log[i]['total_vists']
        keep.append(travel_log[i])

print(keep)

## this will not work
# print(travel_log[1]['country']['citied_visited'])
# two venues, artists perform in both venues but others in just one
#ensure no scheduling conflict
#function takes two dictionaries, scheduling of both venues maping
#performing time to the artist

#empty dict
#iterate in the first venue,
# using the key - the artist name
#check if that same key is available in the second venue
# if that artist is performing in the second venue check the time of the value in the second venue item
# if it is the same add is to the result dictionary

def identify_conflicts(venue1_schedule, venue2_schedule):
    res = {}

    for i in venue1_schedule.items():
        artist = i[0]
        if artist in venue2_schedule:
            if venue2_schedule[artist] == i[1]:
                res[artist] = i[1]
    return res

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
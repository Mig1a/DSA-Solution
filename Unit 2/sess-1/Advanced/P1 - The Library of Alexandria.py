#function takes two args 1. a dict with rooms names and scroll capcity
#2. room names and actual scroll distribution
# return available space + int or over capacity - int in a dict pairing it with room name

#create an empty dict holding the result
#iterate through the catalog and calcuale the differnce and add it to the dict


def analyze_library(library_catalog, actual_distribution):
    res = {}

    for i in library_catalog.keys():
        res[i] = actual_distribution[i] - library_catalog[i]

    return res

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))
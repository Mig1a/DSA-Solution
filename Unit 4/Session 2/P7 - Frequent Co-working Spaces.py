"""
function takes 1 arg,

1. a list of str - representing a list of co-working spaces

process the frequency of visit for each work spaces

return the max visited work spaces

create a dict
iterate through and add the items in the the dict with their freq count
use max and get the max frequently visited place
"""

def most_frequent_spaces(visits):
    count = {}

    for i in visits:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    s = sorted(count.items(), key=lambda x:x[1], reverse=True)
    maxnum = s[0][1]

    return [space for space,val in s if val == maxnum]
visits = ["WeWork", "Regus", "Spaces", "WeWork", "Regus", "WeWork"]
print(most_frequent_spaces(visits))

visits_2 = ["IndieDesk", "Spaces", "IndieDesk", "WeWork", "Spaces", "IndieDesk", "WeWork"]
print(most_frequent_spaces(visits_2))

visits_3 = ["Hub", "Regus", "WeWork", "Hub", "WeWork", "Regus", "Hub", "Regus"]
print(most_frequent_spaces(visits_3))
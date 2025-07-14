# function takes 2 arguments of str lists equal length
# map the item from set_times to artists at the same index
#output artist[i]:set_times[i] as an object as key and values pair

# A variable with empty dictionary that holds the pairs
# a for loop that iterate either of the arguments length times
# in every iteration pick items from both parameters and
# add it to the dictionary as a key value pair
# return the whole dictionary
def lineup(artists, set_times):
    res = {}
    for i in range(len(artists)):
        res[artists[i]] = set_times[i]
    return res

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
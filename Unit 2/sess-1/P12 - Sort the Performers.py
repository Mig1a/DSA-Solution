# function takes 2 arg one artist names and their performing durations in miniutes
# both args same length, artist[i] denotes duration[i]
# return artists names sorted by the duration descendigly

# create a dict var
# check if the length of the args are equal
# iterate len of artists times, and add the artist an its correspondant dur to the dict
# sort the dict based on the duraion max to min
# return the keys

def sort_performers(performer_names, performance_times):


    if len(performer_names) != len(performance_times):
        return "length not equal"

    res = list(zip(performer_names,performance_times))


    res.sort(key=lambda x:x[1], reverse=True)
    so = [name for name,i in res]


    return so

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1))
print(sort_performers(performer_names2, performance_times2))

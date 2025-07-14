#function takes 2 args, a list of str and an int,
#return the str present in the list under the int times

#create a variable dict
#add the str to the list and add their presence
#filter the str more than the threshold

def declutter(souvenirs, threshold):
    store = {}

    for i in souvenirs:
        if i in store:
            store[i] += 1
        else:
            store[i] = 1
    res = [s for s in souvenirs if store[s] < threshold]

    return res

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2

print(declutter(souvenirs1,threshold1))
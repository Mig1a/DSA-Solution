#attendees of a festival votes their favourite set
#count the votes and return the top voted artist
#function takes a disctionary attendes ID as a key and their fav artist
#as a values

#create an empty dict
#iterate through the values and add each artist into the dict,
#if artist is already in the ne dict increament their votes

def best_set(votes):
    res = {}

    for i in votes.values():
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    so = sorted(res.items(), key=lambda x:x[1], reverse=True)

    return so[0][0]
votes1 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
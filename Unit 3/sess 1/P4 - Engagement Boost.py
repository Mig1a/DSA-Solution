def engagement_boost(engagements):
    squared_engagements = [] # created a new list to hold the squred items

    for i in range(len(engagements)): #iterate through the num tymes of the orginal list
        squared_engagement = engagements[i] * engagements[i] #stored the squared value
        squared_engagements.append(squared_engagement) # added the squared value for each items in the new list

    squared_engagements.sort() #sorted in ascending order



    return squared_engagements

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

def engagement_boost(engagements):
    result = [] #result holder list
    l,r = 0, len(engagements) -1  #two pointers starting from the begining and end of the list
    while l <= r: #iterate to get each item in the list and end the itreration when l = r
        squared = engagements[l] ** 2
        result.append(squared)
        l += 1

    result.sort() # sort the new squred items in acsending order

    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

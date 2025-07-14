#function takes two arg, 1. a list of int and 2. an int
#every int in the list lesser than the 2nd int comes before
#evry int in the list greater than the 2nd int

#every int in the list equal to the 2nd int, comes between in to the lower and higher int

#3 array's storing the 3 priority types
#iterate through the list and append each item to each array
#return adding each other

def arrange_attendees_by_priority(attendees, priority):
    less = []
    equal = []
    greater = []

    for attendee in attendees:
        if attendee < priority:
            less.append(attendee)
        elif attendee == priority:
            equal.append(attendee)
        else:
            greater.append(attendee)

    return less + equal + greater

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10))
print(arrange_attendees_by_priority([-3,4,3,2], 2))
#function takes 1 arg, a list of ints
#have prepare a list of ints when reveal the num at the front list
#and moving the next num to the back and repeating this process
#till the list is complete
#the output is a list of int in increasing order

def arrange_attendees(attendees):
    attendees.sort()
    result = []

    for i in reversed(attendees):
        if result:
            result.insert(0,result.pop())

        result.insert(0,i)

    return result


print(arrange_attendees([17,13,11,2,3,5,7]))
print(arrange_attendees([1,1000]))
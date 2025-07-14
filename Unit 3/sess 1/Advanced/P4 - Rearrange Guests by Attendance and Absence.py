#function takes one arg, a list of int, even positive and negative numbers
#have reagrrange the items in positive and negative order by starting from positive


#two pointers
#sliding window, if guets[l] > 0 and guests[r] < 0:
#l += 2, r+= 2

#elif guest[l] < 0:
#f = l - r
#while f > 0:

def rearrange_guests(guests):
    p = []
    n = []
    re = []
    for i in guests:
        if i > 0:
            p.append(i)
        else:
            n.append(i)

    for i in range(len(p)):
        re.append(p[i])
        re.append(n[i])
    return re

print(rearrange_guests([3,1,-2,-5,2,-4]))
print(rearrange_guests([-1,1]))




























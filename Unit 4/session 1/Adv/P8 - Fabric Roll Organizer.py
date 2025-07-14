"""
Function takes 1 arg, a list of argument, int
Function have create a list of pairs with smaller differences
and return the list

Declare a variable list
sort the arg
Iterate through the sorted arg, and pick 2 items if available else 1
and append them to the list
return the list

time
sorting - O(n log n) log linear
iterating O(n)
append O(1)

space
var O(n)
prep O(n/2)
"""

def organize_fabric_rolls(fabric_rolls):
    result = []
    fabric_rolls.sort(reverse=True)
    while len(fabric_rolls) > 0:
        if len(fabric_rolls) >= 2:
            k = (fabric_rolls.pop(),fabric_rolls.pop())
            result.append(k)
        else:
            result.append(fabric_rolls.pop())
    return result


fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))
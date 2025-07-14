"""
Function takes 2 arg, 1 a list of fabrics - a str and int for each fabric
2nd a list of int representing a fabric roll length
return the difference between the fabric roll and the required fabric for the clothing


declare a var to store the sum of the fabric length
iterate through the items and add the int to the var
return sum(fabric_rolls) - g var

time - O(n) - iterates n number of times
space - O(n) for var,
"""

def calculate_fabric_waste(items, fabric_rolls):
    count = 0
    for i in items:
        count += i[1]

    return sum(fabric_rolls) - count

items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls1 = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls2 = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls3 = [7, 5, 5]

print(calculate_fabric_waste(items, fabric_rolls1))
print(calculate_fabric_waste(items_2, fabric_rolls2))
print(calculate_fabric_waste(items_3, fabric_rolls3))
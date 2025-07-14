"""
Function takes 2 arg, one a list of fabric with their associated cost
another one a budget
have to return 2 fabrics where their cost sum not exceeding the budget

first sort the fabrics based on their cost acsedingly
create a dict
iterate through the sorted fabrics and add their cost difference from budget to the dict
difference:fabric
and check the difference and the cost match if matched return the value of the dnce
and the incaming fabric
"""


def find_best_fabric_pair(fabrics, budget):
    best_pair = ()
    max_cost = -1

    for i in range(len(fabrics)):
        for j in range(i + 1, len(fabrics)):
            name1, cost1 = fabrics[i]
            name2, cost2 = fabrics[j]
            total = cost1 + cost2

            if total <= budget and total > max_cost:
                max_cost = total
                best_pair = (name1, name2)

    return best_pair if best_pair else None
fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

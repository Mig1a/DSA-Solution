"""
function takes 1 arg, a list of tuple with fabric-str and rating - int
function have to proces and return a list of fabric based on thier rating
from low rating on the top [-1] to top rated fabric [0]

sort the tuple based on the ratings descendingly
create an empty list
iterate and add the fabrics to a list based on the sorting
return the list
"""


def organize_fabrics(fabrics):
    result = []
    cont = {}
    for i in fabrics:
        if not result:
            result.append(i[0])
            cont[i[0]] = i[1]
        else:
            if cont[result[-1]] > i[1]:
                result.append(i[0])
                cont[i[0]] = i[1]
            else:
                k = []
                while result:
                    if cont[result[-1]] < i[1]:
                        k.insert(0,result.pop())
                    else:
                        break
                result.append(i[0])
                result.extend(k)
                cont[i[0]] = i[1]

    return result
fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))
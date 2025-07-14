#function takes 1 argument of 2d list of int, races[i] = winner , losser
#indicating the winner defeated the loser
#return a 2-2d array, the first array with winners who have not lost any race
#and the second array with travelers who only loose once

#create a empty dict
#iterate through the races add the winner or losser as a key and with conditionals add an array
#of two items to track thier winning and lossing
#iterate through the dict and collect the non losssing and one time lossers


def find_travelers(races):
    cont = {}

    for i in races:
        if i[0] in cont:
            cont[i[0]][0] += 1
        elif i[0] not in cont:
            cont[i[0]] = [1,0]
        if i[1] in cont:
            cont[i[1]][1] += 1
        elif i[1] not in cont:
            cont[i[1]] = [0,1]
    print(cont)
    res = [[],[]]
    for i,k in cont.items():
        if k[1] == 0:
            res[0].append(i)
        elif k[1] < 2:
            res[1].append(i)
    return res

races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))
print(find_travelers(races2))
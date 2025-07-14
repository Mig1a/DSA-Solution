#function takes 2 arg, 1. a target meal - str, 2. ingredients - str
#returns how many targeted meals can be created with the availaible ingredients


#create a dict with the target meals str, each letter as a key and 0 value
#itreate through the ingredients and when there is a macth with targeted meals character
#add on that
#sort the dict ascendigly return the first item


def max_attempts(ingredients, target_meal):
    cook = {}
    for i in target_meal:
        cook[i] = 0
    for i in ingredients:
        if i in cook:
            cook[i] += 1
    so = sorted(cook.items(),key=lambda x:x[1])
    print(cook)
    return so[0][1]

ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"

print(max_attempts(ingredients1,target_meal1))
print(max_attempts(ingredients2,target_meal2))
print(max_attempts(ingredients3,target_meal3))
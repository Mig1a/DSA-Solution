#function takes two arg
# 1.arrenged list of artists performance in a specific stage
# 2. a permutated or the same list different arrengment list of artists in a different stage

# the stage difference for a specific artist is defined by the absolute value difference in
# index from the first and second stages

# function have to return the sum of differences for all artists

#dict variable to store the index
# iterate and add the index to the dict for the first stage
#create a variable to track the sum
# iterate through the second stage artists and calculate the absolute value in the dict
#add the value tp the result variable

def find_stage_arrangement_difference(s, t):
    di = {}

    for i,k in enumerate(s):
        di[k] = i

    res = 0
    for i,k in enumerate(t):
        if di[k] == i:
            continue
        else:
            su = abs(i - di[k])
            res += su

    return res

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))


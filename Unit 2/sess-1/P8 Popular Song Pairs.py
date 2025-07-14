#create a dict
#iterate the argument, add each item or increase if present
#create a result variable
#iterate the dict calculate the number of pairs and add is to the result
def num_popular_pairs(popularity_scores):
    d = {}

    for i in popularity_scores:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    result = 0
    for i in d.values():
        k = (i * (i-1)) // 2
        result += k

    return result

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))
#function takes an array with positive int
#return by adding the largest int

def max_audience_performances(audiences):
    max_int = max(audiences)
    count = 0
    for i in audiences:
        if i == max_int:
            count += 1
    return max_int * count

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
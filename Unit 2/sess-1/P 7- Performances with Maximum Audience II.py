def max_audience_performances(audiences):
    res = {}

    for i in audiences:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    so = sorted(res.items(), key=lambda x:x[0], reverse=True)

    return so[0][0] * so[0][1]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
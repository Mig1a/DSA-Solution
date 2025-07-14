def find_closest_nft_values(nft_values, budget):
    min = float('-inf')
    max = float('inf')
    res = []

    for i in nft_values:
        if i > min and i < budget:
            min = i
        if i > budget and i < max:
            max = i
    res.append(min)
    res.append(max)


    return res

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
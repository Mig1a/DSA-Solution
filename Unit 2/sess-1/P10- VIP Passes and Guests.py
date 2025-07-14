def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for i in vip_passes:
        vip_set.add(i)
    count  = 0

    for i in guests:
        if i in vip_set:
            count += 1

    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

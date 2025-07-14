#function takes 1 arg, a list of int
#check for the current item at which index is the higher number is

#create a list [0] * len[dt] -1
#iterate through len dt, k = i while k + 1 < len[dt] -1:
#if dt[k] > dt[i]: list[i] = k - i pass
#return list

def time_to_complete_dream_designs(design_times):
    res = [0] * len(design_times)
    for i in range(len(design_times) -1):
        k = i + 1
        while k <= len(design_times):
            if design_times[k] > design_times[i]:
                res[i] = k - i
                break
            k += 1
    return res

print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3]))
print(time_to_complete_dream_designs([2, 3, 1, 4]))
print(time_to_complete_dream_designs([5, 5, 5, 5]))
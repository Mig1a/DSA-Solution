#function takes 1 arg, a list of int,
#the sequence is a circular sequence, the first ietem is the next item
#for the last item,
#for each items find the greatest items in the sequence, if no greater item store -1

#traverse the list and iterate again when we find a greater item add that to the result list
#return the result

def next_greater_dream(dreams):
    res = [-1] * len(dreams)

    for i in range(len(dreams)):
        for k in range(i,i + len(dreams)):
            if dreams[k % len(dreams)] > dreams[i]:
                res[i] = dreams[k % len(dreams)]
                break
    return res

print(next_greater_dream([1, 2, 1]))
print(next_greater_dream([1, 2, 3, 4, 3]))

def next_greater_dream_elements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # will store indices

    for i in range(2 * n - 1, -1, -1):
        current_index = i % n
        current_val = nums[current_index]

        # Maintain decreasing stack
        while stack and nums[stack[-1]] <= current_val:
            stack.pop()

        if stack:
            res[current_index] = nums[stack[-1]]

        stack.append(current_index)

    return res
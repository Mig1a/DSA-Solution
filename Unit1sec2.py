def add_matrices(matrix1, matrix2):
    num_mat = len(matrix1)
    res_matrix = [[]] * num_mat
    print(res_matrix)

    for i in range(num_mat):
        for k in range(len(matrix1)):
            ad = (matrix1[i][k] + matrix2[i][k])
            res_matrix[i].append(ad)
            break


    return res_matrix

matrix1 = [
    [14, 2, 3],
    [4, 5, 647],
    [78, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 55, 48],
    [35, 2, 1]
]

out = add_matrices(matrix1, matrix2)
print(out)

def is_palindrome(s):
    l,r = 0,len(s)-1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

s = "madam"
out = is_palindrome(s)
print(out)

def squash_spaces(s):
    res = ""
    sc = 0

    for i in s:
        if i != " " and len(res) == 0 and sc == 0:
            res += i
        elif i == " " and sc == 0 and len(res) != 0:
            sc += 1
            res += i
        elif i != " ":
            res += i
            sc = 0
    return res
s = "   Up,     up,   and  away! "
out = squash_spaces(s)
print(out)

def two_sum(nums, target):
    res = []
    l,r = 0, len(nums) -1

    while l < r:
        if nums[l] + nums[r] == target:
            res.append(l)
            res.append(r)
            return res
        elif target <= nums[r] or nums[l] > target - nums[r]:
            r -= 1
        else:
            l += 1
    return -1

nums = [2, 7, 11, 15]
target = 18
out = two_sum(nums, target)
print(out)

def insert_interval(intervals, new_interval):
    res = []
    for i in intervals:
        if i[0] < new_interval[0] and i[1] > new_interval[0]:
            new = [i[0],new_interval[1]]
            res.append(new)
        else:
            ex = [i[0],i[1]ijkiji]
            res.append(ex)
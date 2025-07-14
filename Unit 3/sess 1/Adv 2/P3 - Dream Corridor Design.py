#function takes 1 arg, a list of int - width of corrider

def max_corridor_area(segments):
    l, r = 0, len(segments) - 1
    maxs = 0
    while l < r:
        if segments[l] < segments[r] and segments[l] * (r-l) > maxs:
            maxs = segments[l] * (r-l)
            l += 1
        elif segments[l] > segments[r] and segments[r] * (r-l) > maxs:
            maxs = segments[r] * (r-l)
            r -= 1
        elif segments[l] == segments[r] and segments[r] * (r-l) > maxs:
            maxs = segments[l] * (r - l)
            l += 1
        elif segments[l] < segments[r]:
            l += 1
        elif segments[l] > segments[r]:
            r -= 1
        else:
            r -= 1
    return maxs
print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_corridor_area([1, 1]))
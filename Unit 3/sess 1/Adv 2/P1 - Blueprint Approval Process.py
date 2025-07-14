#function takes 1 arg, a list of int, representing a complexity level
def blueprint_approval(blueprints):
    queue = blueprints[:]
    res = []
    so = sorted(blueprints)

    while so:
        k = queue.pop(0)
        if k == so[0]:
            res.append(k)
            so.pop(0)
        else:
            queue.append(k)
    return res


print(blueprint_approval([3, 5, 2, 1, 4]))
print(blueprint_approval([7, 4, 6, 2, 5]))
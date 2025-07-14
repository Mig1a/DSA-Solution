#function takes two arg, both a str
#in both args there is a # which is considered a backspace
#after the processing the backspaces compare the len of the args
#return true if equal and false if not

def post_compare(draft1, draft2):
    res = [[],[]]

    for i in draft1:

        if i == '#' and len(res[0]) == 0:
            res[0].pop()
        else:
            res[0].append(i)
    for i in draft2:

        if i == '#' and len(res[1]) == 0:
            res[1].pop()
        else:
            res[1].append(i)

    return len(res[0]) == len(res[1])

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#"))
print(post_compare("a#c", "b"))
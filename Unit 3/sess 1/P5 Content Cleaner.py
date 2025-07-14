def clean_post(post):
    res = []
    for i in post:
        if not res:
            res.append(i)
        else:
            if res[-1].upper() == i:
                res.pop()
            else:
                res.append(i)
    return ''.join(res)

print(clean_post("poOost"))
print(clean_post("abBAcC"))
print(clean_post("s"))
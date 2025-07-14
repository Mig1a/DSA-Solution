#function takes 1 arg, a str
#reverse the words reserving their orders and spaces
#return a reversed str

#split the str
#iterate through it and reverse it using slicing
#join and retirn the str

def edit_post(post):
    s = post.split()
    res = []
    for i in s:
        res.append(i[::-1])

    return ' '.join(res)

print(edit_post("Boost your engagement with these tips"))
print(edit_post("Check out my latest vlog"))

rev = ''
h = ['n','k','k']
while h:
    rev = h.pop(0) + rev
    print(rev)

print(rev)
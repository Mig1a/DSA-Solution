#function takes one arg, a str
#return true or false if the string is the same reading forward and backward
#ignore spaces and other characters

#iterate and store the just the letters in a str use isalnum()
#create two pointers
#check is both sides are same


def is_symmetrical_title(title):
    st = ''

    for i in title:
        if i.isalnum():
            st += i.lower()

    l,r = 0 ,len(st) -1
    while l < r:
        if st[l] != st[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))

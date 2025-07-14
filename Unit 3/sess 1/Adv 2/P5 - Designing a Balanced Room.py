#function takes an argument, a str with lettter and bracket char
#remove an unbalanced bracket from the str

#create a stack,
#create a new str
#iterate through and if the item is alnum just add it to the new str
#if stack is empty and item ). just pass
#if item ( add it to the stack
#if item ), stack.pop() and add ) to str


def make_balanced_room(s):
    st = []
    res = []

    for i, char in enumerate(s):
        if char.isalpha():
            res.append(char)
        elif char == '(':
            st.append(len(res))  # store index in res
            res.append(char)
        elif char == ')':
            if st:
                st.pop()
                res.append(char)
            # else: skip unmatched ')'

    # Remove unmatched '(' using stored indexes
    for i in st:
        res[i] = ''  # mark for removal

    return ''.join(res)

print(make_balanced_room("art(t(d)e)sign)"))
print(make_balanced_room("d)e(s)ign"))
print(make_balanced_room("))(("))
#function takes one arg, a string
#function have to process and provide the number symbol to make it full

#a dict with ):(
#a stack
#var = 0
#iterate through the arg
#if not stack and i ): var += 1
#elif i == (: append to stack
#else: pop from stack
#return var + len(stack

def min_changes_to_make_balanced(schedule):
    st = []
    var = 0

    for i in schedule:
        if not st and i == ')':
            var += 1
        elif i == '(':
            st.append(i)
        else:
            st.pop()

    return var + len(st)

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("((("))
#function takes 1 arg, a string
#based on the arg, if a chr is I the next number should be higher prev
#if D next number should be smaller from the prev
#return a str, if arg[i] == I, return[i] < return[i+1]
#but arg[i] == D, return [i] > return[i]

def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    result = []

    n = len(arrival_pattern)

    for i in range(n+1):
        stack.append(i+1)

        if i == n or arrival_pattern[i] == 'I':

            while stack:
                result.append(stack.pop())

    return ''.join(str(result))


print(arrange_guest_arrival_order("IIIDIDDD"))
print(arrange_guest_arrival_order("DDD"))

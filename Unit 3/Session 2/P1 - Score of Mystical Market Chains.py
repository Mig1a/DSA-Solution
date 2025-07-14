#function takes 1 arg, a str -  a bracket
#count balanced bracket,

#create a count var
#create a list
#traverse through the arg and add to the stack and count when ( and pop from stack when stack-1 (
#if stack return -1
#return count

def score_of_mystical_market_chains(chain):
    stack = []

    for char in chain:
        if char == '(':
            stack.append(char)
        else:  # char == ')'
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                stack.pop()  # pop the matching '('
                stack.append(2 * temp)
        print(stack)
    return sum(stack)

print(score_of_mystical_market_chains("()"))
print(score_of_mystical_market_chains("(())"))
print(score_of_mystical_market_chains("(()(()))"))
print(score_of_mystical_market_chains("()()"))

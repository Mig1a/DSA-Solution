#function takes one argument, a list of str
#reverse the list and return them

#create a new list
#iterate through the list with while loop
#pop the last item from the list and store it in a var
#append the var in a new list
#return the new list

def reverse_comments_queue(comments):
    res = []
    s = 0
    while s < len(comments):
        res.append(comments.pop())
    return res
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
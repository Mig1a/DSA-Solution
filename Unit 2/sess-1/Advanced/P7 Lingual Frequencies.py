#function takes 2 args, 1 . a str and a list of str
#find the word with max presence and check that word is in the illegibles,
#if not return that word

#split the sentence to acces each words
#create a dict, count each word
#sort the dict by the count
#check the max count word is in illegible list, if not return the word,
# if continue looking

def find_most_frequent_word(text, illegibles):
    word = text.split()
    cont = {}
    for i in word:
        cw = i.upper().rstrip(",.")
        if cw in cont:
            cont[cw] += 1
        else:
            cont[cw] = 1

    y = sorted(cont.items(), key=lambda x:x[1], reverse=True)
    for i in y:
        if i[0].lower() not in illegibles:
            return i[0].lower()
paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1))

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2))
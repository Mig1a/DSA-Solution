# function takes 3 args,
#1. list of str, 2. list of str 3. 2d array with "two similar" str
#function have to check the length of 1 and 2 are equal
#1[i] and 2[i] have to be present in similar[i]
#return boolean based on these condition


#if len(sent1) != len(sent1) False
#iterate len sent1 times check if sent1[i] and sent[i] are the same
# if the same continue, if not
#create a str list var
#iterate through simlar pairs and check if these pairs are available
#if the pairs are availabe break if not return False
#Return True

def is_similar(sentence1, sentence2, similar_pairs):
    if len(sentence1) != len(sentence2):
        return False
    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i]:
            continue
        pair = [sentence1[i],sentence2[i]]
        print(pair)
        if pair in similar_pairs:
            continue
        else:
            return False
    return True

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))

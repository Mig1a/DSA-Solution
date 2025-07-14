"""
function takes 1 arg,
1. a sentence - str

function have count the frequency of each word and store, words are case insensitive

and return the frequency of each word and the large frequently used word if tied both

create a cont var dict
split the sentense into word
iterate through the words, make them all small letter
if the word already exist in the cont add its frequency else add the word
use max to get the most largest frequently words
return the cont and the max

"""
def strip_special_chars(s):
    return ''.join(c for c in s if c.isalnum() or c.isspace())
def word_frequency_analysis(text):
    words = strip_special_chars(text).split()
    cont = {}
    for i in words:
        if i.lower() in cont:
            cont[i.lower()] += 1
        else:
            cont[i.lower()] = 1
    m = [max(cont, key=cont.get)]
    return (cont,m)

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))
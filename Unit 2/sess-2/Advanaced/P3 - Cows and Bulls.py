#function takes 2 args. both args are digits
#a secret digit and a guess digit to get the secret digit
#function have to reurn how many accuarte and exact position digits
#and exact but displaced position digits are there
#xAyB x - number of exact and perfectly positioned digit
# y represents number of exact but misplaced digits

#create an empty dict
#check length are equal
#itrate length of secret times
#add the elements of secret to the dict with there indexes as their values
#on the same iteration check the guess in same index is available in the dict and seceret
#if true alter the return index


def get_hint(secret, guess):
    coll = {}
    x = 0
    y = 0
    for i in range(len(secret)):
        if secret[i] not in coll:
            coll[secret[i]] = 1
        else:
            coll[secret[i]] += 1
        if guess[i] == secret[i]:
            x += 1
            coll[secret[i]] -= 1

        elif guess[i] in secret:
            if guess[i] in coll and coll[guess[i]] > 0:
                y += 1
                coll[guess[i]] -= 1
            elif guess[i] not in coll:
                coll[guess[i]] = 0
                y += 1


    return f"{x}A{y}B"
secret1 = "1807"
guess1 = "7810"

secret2 = "1122"
guess2 = "2211"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))


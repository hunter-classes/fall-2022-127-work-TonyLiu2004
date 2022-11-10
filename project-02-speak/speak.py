#Extras:
# - Reads translations from a file
# - Deals with punctuation and capitalized letters
# - Adds random sentences inbetween sentences

import random

pirate = {}
punc = ",.?!:;~-$"

#building the dictionary
with open("pirate.dat", 'r') as file:
    for x in file:
        line = x.strip()
        w1 = line[0:line.find(":")]
        w2 = line[line.find(":") + 1:len(line)]
        pirate[w1] = w2


def pirateSpeak(file):
    ret = ""
    #end = ""
    with open(file, 'r') as file:
        for line in file:
            for word in line.split():
                #puts all punctuation into end, put at the end of word
                upped = False
                if (word[0].isupper()):
                    upped = True
                words = word.lower()
                end = ""
                for p in punc:
                    if (word.find(p) != -1):
                        end = end + p
                        words = words[0:words.find(p)]
                if (word.find(".") != -1):
                    pirateQ = [
                        " Shiver me timbers!", " Walk the plank!", " Arrg!"
                    ]
                    if (random.randint(0, 3) == 0):
                        end = end + pirateQ[random.randint(
                            0,
                            len(pirateQ) - 1)]
                if (words in pirate.keys()):
                    if (upped):
                        ret = ret + pirate[words].capitalize() + end + " "
                    else:
                        ret = ret + pirate[words] + end + " "
                else:
                    if (upped):
                        ret = ret + words.capitalize() + end + " "

                    else:
                        ret = ret + words + end + " "
        return ret


print(pirateSpeak("input.txt"))

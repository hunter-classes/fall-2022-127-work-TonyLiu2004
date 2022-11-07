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
    with open(file, 'r') as file:
        for line in file:
            for word in line.split():
                #puts all punctuation into end, put at the end of word
                words = word
                end = ""
                for p in punc:
                    if (word.find(p) != -1):
                        end = end + p
                        words = words[0:words.find(p)]
                if (words in pirate.keys()):
                    ret = ret + pirate[words] + end + " "
                else:
                    ret = ret + words + end + " "
    return ret


print(pirateSpeak("input.txt"))

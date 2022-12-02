def clean(s):
    letters = []
    for l in s:
        if l.isalpha() or l == ' ' or l == '\n':
            letters.append(l)
    result = "".join(letters)
    result = result.lower()
    return result


def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word, 0)
        counts[word] = counts[word] + 1

    return counts


def get_words_min_max(bag, mincount, maxcount):
    results = []
    for word in bag.keys():
        if bag[word] >= mincount and bag[word] <= maxcount:
            results.append([word, bag[word]])
    return results


def get_words_range(bag, mincount, maxcount):
    results = [[x, bag[x]] for x in bag \
               if bag[x] >= mincount and bag[x] <= maxcount]
    return results


def removeStopWords(bag, sw):
    newBag = {}
    for x in bag:
        if x not in sw:
            newBag[x] = bag[x]
    return newBag


file = open("scandal.txt")
raw_data = file.read()
data = clean(raw_data)
bag = build_bow(data)

file2 = open("NLTKstopwords.txt")
raw_data2 = file2.read()
data2 = clean(raw_data2)
listSW = [x for x in data2.split()]

print(removeStopWords(bag, listSW))
#print(bag)

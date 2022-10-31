import random
import datetime
def findLargest(l):
    i = l[0]
    for x in l[1:]:
        if x > i:
            i = x
    return i


def freq(l, v):
    count = 0
    for x in l:
        if x == v:
            count += 1
    return count


def mode(dataset):
    modes = []
    noDupes = []
    for x in dataset:
        if x not in noDupes:
            noDupes.append(x)

    for y in noDupes:
        modes.append(dataset.count(y))

    ret = []
    for z in range(len(modes)):
        if modes[z] == max(modes):
            if noDupes[z] not in ret:
                ret.append(noDupes[z])
    return ret


def modeEasy(dataset):
    mode = dataset[0]
    for x in dataset[1:]:
        if (freq(dataset, x) > freq(dataset, mode)):
            mode = x
    return mode


def buildRandomList(size, maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result


def testMode(size, maxValue):
    dataset = buildRandomList(size, maxValue)
    # print(dataset)
    t = datetime.datetime.now()
    starttime = t.microsecond / 1000
    m = mode(dataset)
    end = datetime.datetime.now()
    elapsed = (end.microsecond / 1000) - starttime
    print("size: ", size, " time: ", elapsed)


list = [1, 2, 34, 23, 2, 12, 2]
list2 = [1, 2, 3, 12, 1, 3, 2, 12, 5, 3, 12, 1]
#print(findLargest(list))
#print(freq(list, 2))
#print(mode(list2))
#print(modeEasy(list2))
print(testMode(20000,10))

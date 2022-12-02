def average(numlist):
    count = 0
    sum = 0
    for x in numlist:
        sum += x
        count += 1
    return sum / count


def sum_of_squares(xs):
    ret = 0
    for x in xs:
        ret += x * x
    return ret

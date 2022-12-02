def max(lst):
    max=0
    for x in lst:
        if x > max:
            max = x
    return max

def countOdd(lst):
    return len([i for i in lst if i%2==1])


def sumEven(lst):
    return sum([i for i in lst if i%2==0])
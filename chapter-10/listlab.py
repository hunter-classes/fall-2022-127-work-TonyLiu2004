def listKfind(l1):
  return min(l1)

def listOdd(l1):
  return [i for i in l1 if i%2==1]

def capAll(s1):
  return s1.upper()

def capWordsLongerThan5(s1):
  ret = ""
  for x in s1.split():
    if len(x) > 5:
      ret = ret+ x.capitalize() + " "
    else:
      ret = ret+ x + " "
  return ret

def squareList(l1):
  return [i*i for i in l1]

def add2List(l1,l2):
  if len(l1) >= len(l2):
    return [l1[i] + l2[i] for i in range(len(l1))]
  else:
    return [l1[i] + l2[i] for i in range(len(l2))]

def countWords(l1):
  return len([i for i in l1 if len(i)==5])

def sumUntilEven(lst):
    sum=0
    for x in lst:
        if x%2==0:
            return sum
        else:
            sum+=x
    return sum

def count(lst):
    count=0
    for x in lst:
        if x.lower() == "sam":
            return count+1
        else:
            count+=1
    return count
  
t1 = [-10,-4,-3,0,1,2,3,10,12,30,123,4452]
t2 = [10,9,4,1,-3,4,5,67,7,12,5,-1003]
t3 = [1,3,5,7,10]
strList = ["Cookies","Baguette","sad","gromp","projects","sAm","hmmmm"]
str1="I like cookies! However, I am unable to can eat cookies due to my inability to attain some."

print("find smallest value:", listKfind(t1), "\n -----")

print("list of Odds: ", listOdd(t1), "\n -----")

print("Fully capitalized string: " + capAll(str1), "\n -----")

print("Capitalize words that are longer than 5: " + capWordsLongerThan5(str1), "\n -----")

print("Square every item in list:\nBefore: ",t1,"\nAfter:", squareList(t1), "\n -----")

print("Corresponding values of two lists added: \nlist 1: ",t1,"\nlist 2: ",t2,"\nAdded: ",add2List(t1,t2),"\n------" )

print("Number of words in a list with length of 5: \nList: ",strList,"\nCount: ",countWords(strList),"\n-----")

print("Sum all the elements in a list up to but not including the first even number:\nlist; ",t3,"\nSum up to first even: ",sumUntilEven(t3),"\n-----")

print('Count how many words occur in a list up to and including the first occurrence of the word “sam”:\nList:',strList,"\nCount: ",count(strList))
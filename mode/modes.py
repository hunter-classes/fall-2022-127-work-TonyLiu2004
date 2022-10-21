def findLargest(l):
  i=0
  for x in l:
    if x>i:
      i=x
  return i

def freq(l,v):
  count=0
  for x in l:
    if x==v:
      count+=1
  return count
  
list = [1,2,34,23,2,12,2]
print(findLargest(list))
print(freq(list,2))
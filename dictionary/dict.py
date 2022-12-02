#1
def stringLetterCount():
  x = input("Sentence:")
  x = x.lower().replace(" ","")
  dict = {}
  for i in "abcdefghijklmnopqrstuvwxyz":
    dict[i] = 0
  for i in x:
    dict[i]+=1
  for i in dict:
    print(i,dict[i])

#2
def add_fruit(inventory, fruit, quantity):
  if (inventory.get(fruit,0) == 0):
    inventory[fruit] = quantity
  else:
    inventory[fruit] += quantity
#3
def countAlphabet(file):
  f = open(file,'r')
  str = f.read()
  dict = {}
  
  exclude = ",.`~!@#$%^&*()_+-=1234567890[]{}\|;:/?<>\"\'"
  for x in exclude:
    str=str.replace(x,"")

  for x in str.split():
    x=x.lower()
    if (dict.get(x,0)==0):
      dict[x] = 1
    else:
      dict[x] +=1
  print(dict)

    
    
  

#1 Test
#stringLetterCount()  

#2 Test
#new_inventory = {}
#add_fruit(new_inventory, 'strawberries', 10)
#print('strawberries' in new_inventory)
#print(new_inventory['strawberries'])
#add_fruit(new_inventory, 'strawberries', 25)
#print(new_inventory['strawberries'])

#3 Test
#countAlphabet("alice.txt")
  
dt = {"abc":[1,2,3], "def":[4,5,6],"ghi":[7,8,9]}
dt["abc"][0] = 10
k = dt.keys()
#print(k)
#for item in k:
  #print('person[',item,'] = ',dt[item])
#yt = ("helo",123,345)
#a,b,c = yt
#print(a)
#print(b)
#print(c)
def countWords(s):
  counts={}
  for word in s.split():
    counts.setdefault(word,0)
    counts[word]= counts[word]+1
  return counts

str="Testing count words, should count all the words here and put the word and the count into a dictionary and return it. The english essay is going to give me a headache, I do not want to do it but I have to. I have math class today and I do not want to go."
print(countWords(str))
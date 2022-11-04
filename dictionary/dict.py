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
countAlphabet("alice.txt")
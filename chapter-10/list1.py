myList = []


myList.append(76)
myList.append(92.3)
myList.append("hello")
myList = myList + [True]
myList = myList + [4]
myList = myList + [76]

myList.append(76)
myList.append("apple")
myList.insert(3,"cat")
print("Index of hello: ",myList.index("hello"))
print("Count of 76: ", myList.count(76))
myList.remove(76)
myList.pop(myList.index(True))
print(myList)
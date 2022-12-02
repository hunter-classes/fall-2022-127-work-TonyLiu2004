dictPlayer = {
  "Cookie": 3,
  "Mana":100,
  "Health Potion":[3,1,2],
  "Health":100,
  "Class":"Mage",
  "Weapon":"Wand",
  "isAwakened":False
}

for x in dictPlayer:
  print(x)
  print(dictPlayer[x])
print(dictPlayer["Health Potion"][2])
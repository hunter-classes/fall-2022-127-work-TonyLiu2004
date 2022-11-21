import csv

dict = {}
keys = [] 
def makeDict(file):
  global keys 
  with open(file, 'r') as f:
    reader = csv.reader(f)
    keys = next(reader)
    n = 0
    for row in reader:
      if(n < 10001):
        tempDict = {}
        for x in range(len(keys)):
          tempDict[keys[x]] = row[x]
        dict[n] = tempDict
      else:
        break
      n+=1
  f.close()

def avgPerTeam():
  dictAvgs = {}
  for games in dict:
    for k in keys:
      dictAvgs.setdefault(k,0)
      dictAvgs[k] += float(dict[games][k])
  for key in dictAvgs.keys():
    dictAvgs[key] /= 10000
  return dictAvgs



makeDict("lol.csv")
avgStats = avgPerTeam()
for x in avgStats:
  print(x,avgStats[x])
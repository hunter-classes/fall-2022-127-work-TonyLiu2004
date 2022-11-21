import csv
import matplotlib.pyplot as plt


dict = {}
keys = [] 
def makeDict(file): # creates a dictionaries with the key as the game number from 1 to 10000 and the data is a dictionary with each stat
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

def avgPerTeam(): #Average of all the stats
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
del avgStats["gameId"] #Don't need game ID
for x in avgStats:
  print(x,avgStats[x])



plotDict = avgStats.copy()
del plotDict["blueTotalGold"]
del plotDict["blueTotalExperience"]
del plotDict["redTotalGold"]
del plotDict["redTotalExperience"]
del plotDict["blueGoldPerMin"]
del plotDict["redGoldPerMin"]
del plotDict["blueTotalMinionsKilled"]
del plotDict["redTotalMinionsKilled"]
plt.title("LOL Average Stats Blue vs Red (10000 games)")
plt.xlabel("Stats")
plt.xticks(rotation = 90)
plt.bar(plotDict.keys(),plotDict.values(),color=['blue','red'])
plt.show()
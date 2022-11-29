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

avgStats["redWins"] = 1-avgStats["blueWins"] #redWins not included because it can be inferred from blueWins since there are only 2 teams
#plotDict = avgStats.copy()
#del plotDict["blueTotalGold"]
#del plotDict["blueTotalExperience"]
#del plotDict["redTotalGold"]
#del plotDict["redTotalExperience"]
#del plotDict["blueGoldPerMin"]
#del plotDict["redGoldPerMin"]
#del plotDict["blueTotalMinionsKilled"]
#del plotDict["redTotalMinionsKilled"]
#plotDict["redWins"] = 1- plotDict["blueWins"]
#print("--------------------")
#print(plotDict)

plotDict = {}
unused = {}
for x in avgStats.keys():
  if("blue" in x):
    plotDict[x] = avgStats[x]
    temp = x.replace("blue","red")
    plotDict[temp] = avgStats[temp]

print("------------End of Statistics--------------")

#deleting information that is too large for graph and appends them to unused
toBeDeleted = []
for keys in plotDict.keys():
  for doNotInclude in ["TotalGold","TotalExperience","GoldPerMin","TotalMinionsKilled","JungleMinionsKilled","ExperienceDiff","CSPerMin","WardsPlaced","GoldDiff"]:
    if doNotInclude in keys:
      unused[keys] = plotDict[keys]
      toBeDeleted.append(keys)
for x in toBeDeleted:
  del plotDict[x]

#plt.title("LOL Average Stats Blue vs Red (10000 games)")
#plt.xlabel("Stats")
#plt.xticks(rotation = 90)
#plt.bar(plotDict.keys(),plotDict.values(),color=['blue','red'])
#plt.show()

#testing 1
#figure, axis = plt.subplots(2)
#axis[0].set_title("g1")
#axis[0].bar(plotDict.keys(),plotDict.values(),color=['blue','red'])
#axis[0].xticks(rotation = 90)
#axis[1].set_title("g2")
#axis[1].bar(unused.keys(),unused.values(),color = ['blue','red'])
#axis[1].xticks(rotation = 90)
#plt.show()
#end testing 1

#testing 2
plot1 = plt.subplot2grid((1,4),(0,0),colspan=2,rowspan=1) # add rotation here?
plot2 = plt.subplot2grid((1,4),(0,2),colspan=2,rowspan=1)

plot1.bar(plotDict.keys(),plotDict.values(),color = ['blue','red'])
plot1.set_title("g1")
plot1.set_xticklabels(plotDict.keys(),rotation = 90)

plot2.bar(unused.keys(),unused.values(),color = ['blue','red'])
plot2.set_title("g2")
plot2.set_xticklabels(unused.keys(),rotation = 90)

plt.xticks(rotation = 90)
plt.show()
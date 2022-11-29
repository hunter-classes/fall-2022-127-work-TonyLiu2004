import csv
import matplotlib.pyplot as plt

#Analysis: Although the statistics between red and blue are mostly the same, there were some small but noticable differences even with 10000 games;
#Red team had a 50.7% winrate while blue team has a 49.3% winrate
#Blue team has a slightly higher number of wards destoryed (blue 2.7907, red 2.6902 )
#Blue team kills more heralds (boss monster) than red team
#Red team kills more dragons (boss monster) than blue team
#Red team kills more elite monsters (mini-bosses) than blue team
#Blue team gets more first bloods (first kill) than red team

#Summary: Even though data from 10,000 games were collected from games with experienced players,
#there are still small differences in statistics. This may be due to the map layout of the game;
#the boss locations sometimes favor one team over the other because of the terrain near them. 
#Also, sometimes the UI can cover up enemy projectiles which can hinder player performance, but this
#issue is much less relevant to experienced players who have good control over their player cameras.
#However, UI coverings can impact the red team more because red teams starts top right while blue team starts bottom left. (imagine a 2d plane)



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
avgStats["redWins"] = 1-avgStats["blueWins"] #redWins not included because it can be inferred from blueWins since there are only 2 teams
for x in avgStats: # prints all the stats
  print(x,avgStats[x])

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

#original
#plt.title("LOL Average Stats Blue vs Red (10000 games)")
#plt.xlabel("Stats")
#plt.xticks(rotation = 90)
#plt.bar(plotDict.keys(),plotDict.values(),color=['blue','red'])
#plt.show()
#end original

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
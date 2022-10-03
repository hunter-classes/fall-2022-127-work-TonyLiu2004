def piglatin(word):
  v="aeiouy"
  i=".!?,-;'(){}[]-/@"
  ret=word.lower()
  end=""
  for x in ret:
    for y in i:
      if(x==y):
        ret= ret.replace(y,"")
        end=end+y 
    
  if (v.find(ret[0:1]) !=-1 ):
    return ret.capitalize() + "yay"+end
  else:
    return ret[1:].capitalize() + ret[0] + "ay"+end


def initialize():
  name = input("What is your full name?")
  return name[0:1].capitalize() + ". " +name[name.find(" ")+1:len(name)].capitalize()
  

def bondify():
  first = input("What is your first name?")
  last = input("What is your last name?")
  return last.capitalize() + ", " + first.capitalize() + " " + last.capitalize()

#print(initialize())
#print(bondify())

print(piglatin("cookie."))
print(piglatin("M!ons@ter."))
print(piglatin("Easy."))
print(piglatin("Table!"))
def initialize():
  name = input("What is your full name?")
  return name[0:1].capitalize() + ". " +name[name.find(" ")+1:len(name)].capitalize()
  

def bondify():
  first = input("What is your first name?")
  last = input("What is your last name?")

  return last.capitalize() + ", " + first.capitalize() + " " + last.capitalize()

print(initialize())
print(bondify())
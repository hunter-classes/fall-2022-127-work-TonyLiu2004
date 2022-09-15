def is_even(n): # 7
  if ((n%2)== 0):
    return True
  return False

def is_odd(n): # 8
  if((n%2)==1):
    return True
  return False

def is_rightangled(a, b, c): # 10
  if((abs(a**2 + b**2 - c**2))<0.001):
    return True
  return False

def is_rightangled2(a, b, c): # 11
  values=[a,b,c]
  values.sort()
  if((abs(values[0]**2 + values[1]**2 - values[2]**2))<0.001):
    return True
  return False

def hello_name(name):
  return "Hello "+name+"!"

def make_out_word(out, word):
  return out[0:2] + word + out[2:4]

def first_two(str):
  return str[0:2]
  
print(is_even(4))
print(is_odd(67))
print(is_rightangled(0.5,0.4,0.64031))
print(is_rightangled2(0.64031,0.4,0.5))

print(hello_name("Tony"))
print(make_out_word("<!!>","Cookie"))
print(first_two("12345"))
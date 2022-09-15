s1="Hello World"
s2='another\nstring'
s3="""
this is a multi
line string
!!!
"""
print(s1)
print(s2)
print(s3)

s4=s1+s1
print(s4)
print(s1*3)
print(3*s1)

print(len(s1))
print(len("abcde"))

space_location=s1.find(" ")
print(space_location)

s5=s1[space_location+1:]
print(s5)
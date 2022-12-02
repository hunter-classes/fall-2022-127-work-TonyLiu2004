a=input("What is current time?")
b=input("How long do you have to wait?")

curr=int(a)
wait=int(b)

time=(curr+wait)%24

print(time)
import random

rlist = []
for i in range(0, 100):
r = random.randint(0,100)
rlist.append(r)


def checkEven(rlist):
c = 0
for i in range(0, 100):
if(rlist[i] % 2 == 0):
c = c + 1
return c

c = checkEven(rlist)
print("Total number of elements within the given range that are even is: ")
print(c)

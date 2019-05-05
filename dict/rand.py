import random
d={}
for x in range(11):
 num=random.randint(0,11)
 print num
 d[num]=d.get(num,0)+1
print d


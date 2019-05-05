l=[1,2,35,6,33,21,33]
l1=[]
for num in l:
  if num%2!=0:
    ret=num**2
    if ret>50:
      ret1=ret**3
      l1.append(ret1)
print l1

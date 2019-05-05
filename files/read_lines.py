

fp=open("sum.py","r")
for line in fp.readlines():
  print line,
fp.close()
print fp.closed()

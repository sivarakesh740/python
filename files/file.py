
fp=open("sum.py","r")
print fp.name
print fp.mode
print fp.closed
print fp.fileno()
fp.close()
print fp.closed

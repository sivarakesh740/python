import sys
if len(sys.argv)!=2:
  print "usage ./a.out filename"
else:
  fp=open(sys.argv[1],"r+")
  s=fp.read().swapcase()
  print fp.tell()
  fp.seek(0,0)
  fp.write(s)
  fp.close()


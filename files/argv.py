import sys 
if len(sys.argv)!=2:
   print "usage ./a.out filename\n"
else:
   sys.stdout=open(sys.argv[1],"w")
   print "good"  
   print "dsdnfn"








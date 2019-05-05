
try:
  n=input("enter num\n")
  ret=100/n
except ZeroDivisionError as err:
 print err.message
else:
 print "result:",ret
finally:
 print "siva rakesh is good"
 print "great india"

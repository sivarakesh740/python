
try:
  #print l
  #10/0
#  l=[10,20] 
 # print l[10]
  s="vector"
  s[0]='i'

except NameError:
   print "name problem"
except TypeError:
   print "type problem"
except IndexError:
   print "index error"
except ZeroDivisionError:
  print "zero problem"

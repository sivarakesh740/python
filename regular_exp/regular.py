
import re

s="cat are smarter then dogs"
#s="\ncat are smarter then dogs"
#obj=re.match('cat',s)
#obj=re.match('dogs',s)
#obj=re.search('dogs',s)
#obj=re.match('.',s)
#obj=re.match('...',s)
#obj=re.match('.*',s)
#obj=re.match('.+',s)
obj=re.match('.?',s)
if obj:
  print "match found:",obj.group()
else:
  print "match not found"




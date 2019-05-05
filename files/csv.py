
import csv
with open("data","r") as csvfile:
  reader=csv.reader(csvfile)
  field=reader.next()
  print field
  print "*****"
  rec=[record for_ record in reader]
  print rec

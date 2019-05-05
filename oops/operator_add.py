class stud:
 def __init__(self,n,a):
  print "constructor"
  self.name=n
  self.age=a
  self.roll=100
 
 def __str__(self):
   return "name-{} age-{} roll-{}".format(self.name,self.age,self.roll)

 def __add__(self,other):
   return "{} {} {}".format(self.name+other.name,self.age+other.age,self.roll+other.roll)


 def print_fun(self):
   print "name-{} age-{} roll-{}",format(self.name,self.age,self.roll)

 def __del__(self):
   print "destructor"

std=stud("abc",12)
std1=stud("xyz",10)
print std
print std1
print std+std1

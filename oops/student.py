
class student:

 def __init__(self,n,a,k):
   print "costructor"
   self.Name=n
   self.Age=a
   self.roll=k
 
 def print_fun(self):
   print "Name={} Age={} roll={} mark={}".format(self.Name,self.Age,self.roll,self.mark)


 def __del__(self):
   print "destructor"

std=student("adc",12,"v18ce1s11")
std.mark=74.5
std.print_fun()

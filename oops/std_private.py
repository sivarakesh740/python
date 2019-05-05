
class student:
 
 def __init__(self,n,a,m):
   print "constructor"
   self.__name=n
   self.__age=a
   self.roll=m

 def print_fun(self):
   print "name={} age={} roll={} mark={}".format(self.__name,self.__age,self.roll,self.mark)


 def __del__(self):
   print "destructor"

std=student("abc",12,"v18ce1s11")
std.mark=93.3
std.print_fun()
print "roll={} mark={}".format(std.roll,std.mark)




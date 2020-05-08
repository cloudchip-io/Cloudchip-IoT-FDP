

#test code 

import random
import time 
"""
#This is a comment written in more than just one line

x = "Hello World"	                            #str	
x = 20	                                        #int	
x = 20.5	                                    #float	
x = 1j	                                        #complex	
x = ["apple", "banana", "cherry"]	            #list	
x = ("apple", "banana", "cherry")	            #tuple	
x = range(6)	                                #range	
x = {"name" : "John", "age" : 36}	            #dict	
x = {"apple", "banana", "cherry"}	            #set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                                    #bool	
x = b"Hello"	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview

#Setting the Specific Data Type, If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")	                        #str	
x = int(20)	                                    #int	
x = float(20.5)	                                #float	
x = complex(1j)	                                #complex	
x = list(("apple", "banana", "cherry"))	        #list	
x = tuple(("apple", "banana", "cherry"))	    #tuple	
x = range(6)	                                #range	
x = dict(name="John", age=36)	                #dict	
x = set(("apple", "banana", "cherry"))	        #set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	                                    #bool	
x = bytes(5)	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview

+	Addition	            x + y	
-	Subtraction	            x - y	
*	Multiplication	        x * y	
/	Division	            x / y	
%	Modulus	                x % y	
**	Exponentiation	        x ** y	
//	Floor division	        x // y



#if else 

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""


a = "hello"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print(random.randrange(1,10))
print(x)

#input test
input = input()

print(type(input))
print(input)

k = input

print(k)

#String operations
b = "Hello, World!"
print(b[2:5])       # Printing the words between range
print(b[-5:-1])     # Negative Indexing
print(len(b))       # String length

print('Words length', end='')
print(len(b.split()))

print('charaters length', end='')
print(len(b))

# Python code to time demonstration
# working of sleep() 
print("The delay demo") 
 
for x in range(10):
  print(time.ctime())
  time.sleep(10) # using sleep() to hault the code execution 
  

#file example 
#Create file name links.txt(type some text) on the Desktop
filepath = 'links.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()), end='Words : ')
       print(len(line.split()))
       line = fp.readline()
       cnt += 1

if 5 > 2:
    print("Five is greater than two!")
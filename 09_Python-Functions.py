# Databricks notebook source
# MAGIC %md
# MAGIC # Functions

# COMMAND ----------

# MAGIC %md
# MAGIC Purpose: Functions are used to bundle instructions that are needed repeatedly or are too complex to be written as a single block of code. 
# MAGIC
# MAGIC Benefits: Functions make programs more modular and easier to maintain by breaking them into smaller, reusable components. 
# MAGIC Types: There are several types of functions in Python, including built-in functions, user-defined functions, and anonymous functions. 
# MAGIC
# MAGIC
# MAGIC How to create: To create a function, use the def keyword. 
# MAGIC
# MAGIC How to call: To call a function, use the function name followed by parentheses. 
# MAGIC How to pass data: Functions can take parameters, or data, as inputs. 
# MAGIC How to return data: Functions can return data as outputs. 

# COMMAND ----------

def fun(para1,par2)
{
  
}

# COMMAND ----------

def fun_name(parameter1,par2,):
    body

# COMMAND ----------

def wish(name):
   print("hi")
   print("Hello",name," Good Morning")


# COMMAND ----------

#calling
wish("Venkat")

# COMMAND ----------

wish("Python")

# COMMAND ----------

#Write a function to take number as input and print its square value
def squareIt(number):
   print("The Square of",number,"is", number*number)
   


# COMMAND ----------

squareIt(5)

# COMMAND ----------

squareIt(10)

# COMMAND ----------

def addition(x,y):
   return x+y


# COMMAND ----------

addition(10,20)

# COMMAND ----------

#calling
#result=addition(10,20)
#print("The sum is",result)
print("The sum is",addition(100,200))

# COMMAND ----------

#EVEN or ODD
def even_odd(num):
   if num%2==0:
      print(num,"is Even Number")
   else:
      print(num,"is Odd Number")


# COMMAND ----------

#calling
even_odd(100)
even_odd(15)


# COMMAND ----------

#factorial

def factorial(num):
   result=1
   while num>=1:
     result=result*num
     num=num-1
   return result

# COMMAND ----------

print(factorial(4))


# COMMAND ----------

for i in range(1,5):
    print("The Factorial of",i,"is :",factorial(i))

# COMMAND ----------

def sum_sub(a,b):
  sum=a+b
  sub=a-b
  return sum,sub


# COMMAND ----------

sum_sub(10,20)

# COMMAND ----------

x,y=sum_sub(100,50)

print("The Sum is :",x)
print("The Subtraction is :",y)

# COMMAND ----------

def calc(a,b):
   sum=a+b
   sub=a-b
   mul=a*b
   div=a/b
   return sum,sub,mul,div


# COMMAND ----------

t=calc(100,50)
print("The Results are",t)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Different type of arguments

# COMMAND ----------

# There are 4 types are actual arguments are allowed in Python.
#1. positional arguments
#2. keyword arguments
#3. default arguments
#4. Variable length arguments

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. positional arguments

# COMMAND ----------

#These are the arguments passed to function in correct positional order.
def sub(a,b):
  print(a-b)
sub(100,200)
sub(200,100)
#The number of arguments and position of arguments must be matched. If we change the
#order then result may be changed.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Keyword arguments

# COMMAND ----------

#We can pass argument values by keyword i.e by parameter name.
def wish(name,msg):
    print("Hello",name,msg)


# COMMAND ----------

wish(name="BIgdata",msg="Hadoop")
wish(msg="Hadoop",name="BIgdata")
#wish("Hadoop","BIgdata")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Default arguments

# COMMAND ----------

#Sometimes we can provide default values for our positional arguments.
def wish(a,name="Guest",b=200):
   print("Hello",name,"Good Morning",a,b)
   



# COMMAND ----------

wish("10","ABC",20)
wish(10)

# COMMAND ----------

def add(b,a=10):
  return a+b

# COMMAND ----------

add(20)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Variable length Arguments
# MAGIC Sometimes we can pass variable number of arguments to our function,such type of
# MAGIC arguments are called variable length arguments.
# MAGIC We can declare a variable length argument with * symbol as follows
# MAGIC def f1(*n):
# MAGIC We can call this function by passing any number of arguments including zero number.
# MAGIC Internally all these values represented in the form of tuple.

# COMMAND ----------

def sum(*n):
  total=0
  for n1 in n:
    total=total+n1

  print("The Sum=",total)

# COMMAND ----------

#calling
sum(10)
sum(10,20)
sum(20,30,40)
sum(20,30,40,50)

# COMMAND ----------

def f1(*s,n1):
 for s1 in s:
    print(s1)
 print(n1)

# COMMAND ----------

#calling
#f1('A','B',100)#fail
f1('A','B','C',n1=100)
#f1('A','B',arg=200)#fail

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lamda 
# MAGIC Sometimes we can declare a function without any name,such type of nameless functions
# MAGIC are called anonymous functions or lambda functions.
# MAGIC
# MAGIC The main purpose of anonymous function is just for instant use(i.e for one time usage)
# MAGIC
# MAGIC * Normal Function:
# MAGIC We can define by using def keyword.
# MAGIC def squareIt(n):
# MAGIC     return n*n
# MAGIC
# MAGIC
# MAGIC
# MAGIC * lambda Function:
# MAGIC We can define by using lambda keyword
# MAGIC lambda n:n*n

# COMMAND ----------

def sqare(a):
  return a*a


# COMMAND ----------

result=sqare(10)
print(result)

# COMMAND ----------

#Example1
s=lambda n:n*n
print("The Square of 4 is :",s(4))
#print("The Square of 5 is :",s(5))

# COMMAND ----------

#Example2

s=lambda a,b:a+b
print("The Sum of 10,20 is:",s(10,20))

# COMMAND ----------

#Example3

s=lambda a,b:a if a>b else b
print("The Biggest of 10,20 is:",s(10,20))
print("The Biggest of 100,200 is:",s(100,200))

# COMMAND ----------

#MAP FUNCTION:
'''For every element present in the given sequence,apply some functionality and generate
new element with the required modification. For this requirement we should go for
map() function.'''

#Syntax:
#map(function,sequence)
#The function can be applied on each element of sequence and generates new sequence.

# COMMAND ----------

#Eg: Without lambda
lst=[1,2,3,4,5]
def doubleIt(x):
    return 2*x
l1=list(map(doubleIt,lst))
print(l1) 

#[2, 4, 6, 8, 10]

# COMMAND ----------

#with lambda
l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1) #[2, 4, 6, 8, 10]

# COMMAND ----------

#SQARE OF GIVEN NUmber

l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1) #[1, 4, 9, 16, 25]

# COMMAND ----------

#We can apply map() function on multiple lists also.But make sure all list should have same length.

#Syntax: map(lambda x,y:x*y,l1,l2))
#x is from l1 and y is from l2

# COMMAND ----------

l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3) 

# COMMAND ----------

# MAGIC %md
# MAGIC ## REDUCE()
# MAGIC * reduce() function reduces sequence of elements into a single element by applying the
# MAGIC specified function.
# MAGIC * reduce(function,sequence)
# MAGIC reduce() function present in functools module and hence we should write import
# MAGIC statement.

# COMMAND ----------

#reduce() function:
from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result) 

# COMMAND ----------

result=reduce(lambda x,y:x*y,l)
print(result) 

# COMMAND ----------



# COMMAND ----------


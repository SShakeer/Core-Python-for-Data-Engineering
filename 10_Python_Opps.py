# Databricks notebook source
# MAGIC %md
# MAGIC #### What is class?
# MAGIC
# MAGIC 1. In python everything is one object. To create objects we required some Model or Plan or Blue
# MAGIC print, which is nothing but class.
# MAGIC
# MAGIC 1. We can write a class to represent properties (attributes) and actions (behaviour) of object.
# MAGIC
# MAGIC 1. Properties can be represented by variables
# MAGIC 1. Actions can be represented by Methods.
# MAGIC 1. Hence class contains both variables and methods.

# COMMAND ----------

# MAGIC %md
# MAGIC #### How to define class?
# MAGIC 1. We can define a class by using class keyword.
# MAGIC
# MAGIC Syntax:
# MAGIC
# MAGIC class className:
# MAGIC
# MAGIC variables:instance variables,static and local variables
# MAGIC
# MAGIC methods: instance methods,static methods,class methods

# COMMAND ----------

# MAGIC %md
# MAGIC Within the Python class we can represent data by using variables.
# MAGIC
# MAGIC There are 3 types of variables are allowed.
# MAGIC
# MAGIC 1. Instance Variables (Object Level Variables)
# MAGIC
# MAGIC 1. Static Variables (Class Level Variables)
# MAGIC
# MAGIC 1. Local variables (Method Level Variables)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Within the Python class, we can represent operations by using methods. The following are various
# MAGIC types of allowed methods
# MAGIC
# MAGIC 1. Instance Methods
# MAGIC
# MAGIC 1. Class Methods
# MAGIC
# MAGIC 1. Static Methods

# COMMAND ----------

# MAGIC %md
# MAGIC #### Example of class

# COMMAND ----------

class Student:
  def __init__(self):
      self.ename='ABC'
      self.empno=123
      self.salary=100000
  def personal_details(self):
      print('Employee name is',self.ename)
      print('Employee number is',self.empno)
      print('Employee salary is',self.salary)
s=Student()
s.personal_details()

# COMMAND ----------

class Student:
  def __init__(self):
      self.ename='ABC'
      self.empno=123
      self.salary=100000
  def personal_details(self):
      print('Employee name is',self.ename)
      print('Employee number is',self.empno)
      print('Employee salary is',self.salary)
  def addition(self,x,y):
    return x+y
  
s=Student()
s.personal_details()
s.addition(100,300)

# COMMAND ----------

# MAGIC %md
# MAGIC #### What is Object?
# MAGIC
# MAGIC 1. Pysical existence of a class is nothing but object. We can create any number of objects for a class.
# MAGIC
# MAGIC Example: reference variable=classname()

# COMMAND ----------

#Write a Python program to create a employee class and Creates an object to it. Call the
#method personal_details() to display employee details
class Employee:
   def __init__(self,ename,empno,salary):
       self.ename=ename
       self.empno=empno
       self.salary=salary
   def personal_details(self):
       print('Employee name is',self.ename)
       print('Employee number is',self.empno)
       print('Employee salary is',self.salary)


#Instance Creation
s=Employee('ABC',123,100000)
s.personal_details()





# COMMAND ----------

# MAGIC %md
# MAGIC #### Self variable?
# MAGIC
# MAGIC self is the default variable which is always pointing to current object (like this keyword in Java)
# MAGIC
# MAGIC By using self we can access instance variables and instance methods of object.
# MAGIC
# MAGIC
# MAGIC 1. self should be first parameter inside constructor
# MAGIC
# MAGIC def __init__(self):
# MAGIC
# MAGIC
# MAGIC 2. self should be first parameter inside instance methods
# MAGIC
# MAGIC def personal_details(self):
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Constructors
# MAGIC
# MAGIC 1. Constructor is a special method in python.
# MAGIC 1. The name of the constructor should be __init__(self)
# MAGIC 1. Constructor will be executed automatically at the time of object creation.
# MAGIC 1. The main purpose of constructor is to declare and initialize instance variables.
# MAGIC 1. Per object constructor will be exeucted only once.
# MAGIC 1. Constructor can take atleast one argument(atleast self)
# MAGIC 1. Constructor is optional and if we are not providing any constructor then python will provide
# MAGIC default constructor.

# COMMAND ----------

#Program to demonistrate constructor will execute only once per object:

class test:
  def __init__(self):
    print('constructor execution')
  def m1(self):
    print('method execution')



t1=test()
t2=test()
#t3=test()
t1.m1()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Types of Variables in Python Class?
# MAGIC
# MAGIC Inside Python class 3 types of variables are allowed
# MAGIC
# MAGIC 1. Instance Variables (Object Level Variables)
# MAGIC 2. Static Variables (Class Level Variables)
# MAGIC 3. Local variables (Method Level Variables)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. Instance Variable:
# MAGIC
# MAGIC Where we can declare Instance variables:
# MAGIC 1. Inside Constructor by using self variable
# MAGIC 2. Inside Instance Method by using self variable
# MAGIC 3. Outside of the class by using object reference variable

# COMMAND ----------

#Inside Constructor by using self variable:

class Employee:
    def __init__(self):
        self.ename='ABC'
        self.empno=123
        self.salary=100000
e=Employee()
print(e.ename)
print(e.empno)

# COMMAND ----------

#Inside Instance Method by using self variable:
class Test:
   def __init__(self):
     self.a=10
     self.b=20

   def m1(self):
     self.c=30

t=Test()
t.m1()
print(t.__dict__)

# COMMAND ----------

#How to access Instance variables:

#We can access instance variables with in the class by using self variable and outside of the class by
#using object reference.

class Test:

    def __init__(self):
       self.a=10
       self.b=20

    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.display()
print(t.a,t.b)


# COMMAND ----------

# MAGIC %md
# MAGIC ####2. Static Variable:
# MAGIC
# MAGIC 1. If the value of a variable is not varied from object to object, such type of variables we have to
# MAGIC declare with in the class directly but outside of methods. Such type of variables are called Static
# MAGIC variables.
# MAGIC
# MAGIC 2. For total class only one copy of static variable will be created and shared by all objects of that
# MAGIC class.
# MAGIC
# MAGIC 3. We can access static variables either by class name or by object reference. But recommended to
# MAGIC use class name.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Various places to declare static variables:
# MAGIC
# MAGIC 1. In general we can declare within the class directly but from out side of any method
# MAGIC 2. Inside constructor by using class name
# MAGIC 3. Inside instance method by using class name
# MAGIC 4. Inside classmethod by using either class name or cls variable
# MAGIC 5. Inside static method by using class name
# MAGIC

# COMMAND ----------

class Test:

    a=10
    def __init__(self):
       Test.b=20
    def m1(self):
       Test.c=30
    @classmethod
    def m2(cls):
       cls.d1=40
       Test.d2=400
    @staticmethod
    def m3():
        Test.e=50
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)

# COMMAND ----------

class Test:

    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 30
    @classmethod
    def m2(cls):
        cls.d1 = 40
        Test.d2 = 400
    @staticmethod
    def m3():
        Test.e = 50

print(Test.__dict__)
t = Test()
'''print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f = 60
print(Test.__dict__)'''

# COMMAND ----------

#How to access static variables:


1. inside constructor: by using either self or classname
2. inside instance method: by using either self or classname
3. inside class method: by using either cls variable or classname
4. inside static method: by using classname
5. From outside of class: by using either object reference or classnmae

# COMMAND ----------

class Test:
   a=10
   def __init__(self):
       print(self.a)
       print(Test.a)
   def m1(self):
       print(self.a)
       print(Test.a)

   @classmethod
   def m2(cls):
       print(cls.a)
       print(Test.a)
   @staticmethod
   def m3():
       print(Test.a)

       
t=Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()

# COMMAND ----------

# MAGIC %md
# MAGIC #### 3. Local variables
# MAGIC
# MAGIC 1. Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.
# MAGIC
# MAGIC 1. Local variables of a method cannot be accessed from outside of method.

# COMMAND ----------

class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
t=Test()
t.m1()
t.m2()

# COMMAND ----------

class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(a)
        print(b)
t=Test()
t.m1()
t.m2()

# COMMAND ----------

# MAGIC %md
# MAGIC #### We can access members of one class inside another class.

# COMMAND ----------

class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)

class Test:
    def modify(emp):
        emp.esal += 10000
        emp.display()

e = Employee(100, 'Durga', 10000)
Test.modify(e)

#In the above application, Employee class members are available to Test class.

# COMMAND ----------

#example
class Outer:
    def __init__(self):
        print("outer class object creation")
    class Inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")
o=Outer()
i=o.Inner()
i.m1()

# COMMAND ----------

#example 2

class Person:
    def __init__(self):
        self.name = 'Python'
        self.db = self.Dob()

    def display(self):
        print('Name:', self.name)

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 12
            self.yy = 1947

        def display(self):
            print('Dob={}/{}/{}'.format(self.dd, self.mm, self.yy))

p=Person()
p.display()
x=p.db
x.display()

# COMMAND ----------

class Outer:
    def __init__(self):
        print("Outer class object creation")

    class Inner1:
        def __init__(self):
            print("Inner1 class object creation")
        def m1(self):
            print("Inner1 class method")

    class Inner2:
        def __init__(self):
            print("Inner2 class object creation")
        def m2(self):
            print("Inner2 class method")

    class Inner3:
        def __init__(self):
            print("Inner3 class object creation")
        def m3(self):
            print("Inner3 class method")

o = Outer()
i1 = o.Inner1()
i1.m1()
i2 = o.Inner2()
i2.m2()
i3 = o.Inner3()
i3.m3()

# COMMAND ----------

# MAGIC %md
# MAGIC
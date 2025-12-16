# Databricks notebook source
# MAGIC %md
# MAGIC ## Tuple
# MAGIC
# MAGIC Tuple is exactly same as List except that it is immutable. 
# MAGIC i.e once we creates Tuple object,we cannot perform any changes in that object.  
# MAGIC  Duplicates are allowed  
# MAGIC tuple can be created - ()

# COMMAND ----------

[]-list
{}-set
()-tuple

# COMMAND ----------

t=(10,20,20)
print(t)
print(type(t)) 



# COMMAND ----------

#immutability
t=(10,20,30,40)
t[1]=70 

# COMMAND ----------

#index:
t=(10,20,30,40,50,60,70)
print(t[0]) #10 
  
print(t[-1])  #70

# COMMAND ----------

#slice
t=(10,20,30,40,50,60)   
print(t[1:5])
print(t[2:100])
print(t[::2])   

# COMMAND ----------

#concat tuple (+)
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)


# COMMAND ----------

#multiplication (*)
t1=(1,2,3,4,5,6)
t2=t1*10
print(t2)

# COMMAND ----------

#len
t=(1,2,3,4,5,6)
print(len(t))

# COMMAND ----------

#count
t=(10,200,10,110,220)  
print(t.count(10)) #2

# COMMAND ----------

#sorted
t1=(40,10,30,20,100)  
t2=sorted(t1)   
print(t1)
print(t2) 
print(type(t2))  

# COMMAND ----------

t1=sorted(t2,reverse=True) 
print(t1)


# COMMAND ----------

#mix,min

t=(40,10,30,20)   
print(min(t))
print(max(t))

# COMMAND ----------

t=(10,'NAReSH',300)
lst=[10,'SS']
print(t)
print(type(t))
print(lst)
print(type(lst))
# Databricks notebook source
# MAGIC %md
# MAGIC ## Dictionary
# MAGIC * If we want to represent a group of objects as key-value pairs then we should go for Dictionary. 
# MAGIC * Duplicate keys are not allowed but values can be duplicated. 
# MAGIC * Dictionaries are mutable  
# MAGIC * Dictionaries are dynamic  
# MAGIC * indexing and slicing concepts are not applicable 

# COMMAND ----------

#create empty dic
d={}     
#or   
d=dict() 

# COMMAND ----------

print(type(d))

# COMMAND ----------

d={'AP':'Amaravathi','KA':'Bangalore','TS':'Hyderabad'}
print(d)
print(type(d))
print(d['AP'])
print(d['KA'])
print(d['TS'])

# COMMAND ----------

#example
# d={key:value, key:value} 
d={}
d[100]="ABC"  
d[200]="ravi"  
d[300]="Maheer"  
print(d) 
print(type(d))

# COMMAND ----------

d1=()
print(type(d1))

# COMMAND ----------

#We can access data by using keys. 
d={100:'ABC' ,200:'Ruzda', 300:'Maheer'} 
print(d[100])
print(d[200])

# COMMAND ----------

#update-dict
#d[key]=value 
d1={100:"Ravi",200:"Maheer",300:"Ruzda"}
print(d1)
d1[400]="Bangalore"   
print(d1)   
d1[100]="Azure"
print(d1)

# COMMAND ----------

#delete

d={100:"Shakeer",200:"Basha",300:"Hadoop"}
print(d)   
del d[100]
print(d)   
del d[400]   

# COMMAND ----------

#clear
d={100:"Hadoop",200:"Python",300:"Azure"}   
print(d)
d.clear()  
print(d)

# COMMAND ----------

#get: we can get associated value of the key
d={10:"Sk",20:"Basha",30:"Oracle"} 
print(d[20]) 
#print(d[400])
print(d.get(10))
print(d.get(30)) 
print(d.get(10,"Sk")) 
#print(d.get(20,"Basha"))

# COMMAND ----------

 #popitem()-It removes an arbitrary item(key-value) from the dictionaty and returns it.
d={10:"Maheer",200:"Ruzda",300:"abc"}   
print(d)   
print(d.popitem())   
print(d)
print(d.popitem()) 
print(d)

# COMMAND ----------

#print keys from dict
d={100:"Azure",200:"Hadoop",300:"GCP"}   
print(d.keys())   
for k in d.keys():   
    print(k) 

# COMMAND ----------

#print values
d={100:"Azure",200:"Hadoop",300:"GCP"}   
print(d.values())   
for k in d.values():   
    print(k) 

# COMMAND ----------

#items : represents list of key value pairs
d={100:"Hadoop",200:"Data",300:"Engineering"}   
for k,v in d.items():  
    print(k,"<-->",v)

# COMMAND ----------

#Update:
#example:
d = {'id': 10}
d.update({'first_name': 'Donald', 'last_name': 'Duck'})
d.update([('amount', 1000.0), ('commission_pct', 10)])
print(d)

# COMMAND ----------

d

# COMMAND ----------

d.update([('amount', 1500.0), ('commission_pct', 5), ('phone_numbers', 1234567890)])

# COMMAND ----------

d

# COMMAND ----------

d.update([('phone_numbers', [1234567890, 2345679180])])
print(d)

# COMMAND ----------

#Adding

d = {'id': 1, 'first_name': 'Scott', 'last_name': 'Tiger', 'amount': 1000.0}
d['commission_pct'] = 10 # Adding Element
d['phone_numbers'] = 1234567890
print(d)

# COMMAND ----------

d

# COMMAND ----------

#examples
d = {'id': 1, 'first_name': 'Scott', 'last_name': 'Tiger', 'amount': 1000.0}
d['address'] = {'street': '1234 ABC Towers', 'city': 'Round Rock', 'state': 'Texas', 'zip': 78664}


# COMMAND ----------

d

# COMMAND ----------


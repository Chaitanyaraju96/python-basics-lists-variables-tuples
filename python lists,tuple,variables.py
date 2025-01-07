#!/usr/bin/env python
# coding: utf-8

# In[1]:


m2=10


# In[2]:


2m=5


# In[3]:


a=10
a+=10
print(a)


# In[4]:


a=10
a-=10
print(a)


# In[5]:


a=10
a*=10
print(a)


# In[7]:


a=int(input("Enter a number"))
b=int(input("Enter a number"))
print(a+b)


# In[10]:


a=input("Enter a first string: ")
b=input("Enter a second string: ")
print(a+b)


# In[12]:


a=200
b=300
c=400
print(a>b)
print(b>c)
print(a>c)


# In[16]:


otp=int(input("Enter a otp: "))
if otp==100:
    print("Correct,you can start bike ride")
else:
    print("Incorrect,Enter a correct otp to start bike ride")


# In[1]:


a="chaitanya raju"
a[0:5]


# In[2]:


a[10]


# In[3]:


a[0:12:5]


# In[4]:


a[0:10:3]


# In[7]:


a[0:11:-1]
a[0:10:-1]


# In[8]:


a[10:0:-1]


# In[9]:


a[::-2]


# In[9]:


list=[1,2,3,4,"hi","hello"]
print(list)


# In[10]:


list.append("bye")
print(list)


# In[11]:


list.pop(4)
print(list)


# In[13]:


list.remove("hello")
print(list)


# In[15]:


list.extend([8,'virat'])


# In[16]:


print(list)


# In[17]:


list.clear()
print(list)


# In[23]:


l1 = [1, 2, 3, 4]
l2 = ["hi", "hello", "namasthe", "bye"]
final = zip(l1, l2)  # Create a zip object
print(list(final))   # Correct usage of the zip object


# In[24]:


del list


# In[25]:


l1 = [1, 2, 3, 4]
l2 = ["hi", "hello", "namasthe", "bye"]
final = zip(l1, l2)  
print(list(final))  


# In[27]:


list1=[1,2,3,4,5,6]
list(enumerate(list1))


# In[31]:


l1=[23,2,4,5,79,0,85,2,3,5]
print(sorted(l1))


# In[32]:


#tuple


# In[33]:


tuple=(1,2,"hi","hello")
print(tuple)


# In[36]:


print(tuple[0:2])


# In[ ]:





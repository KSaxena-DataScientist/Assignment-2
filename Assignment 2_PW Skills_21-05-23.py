#!/usr/bin/env python
# coding: utf-8

# # Q1. How do you comment code in Python? What are the different types of comments?
# 

# # The commenting in Python is done by using a hash or ''' '''
# # There are two types of commenting:
# # Single line comment: Using hash
# # Multi line comment : using hash in each line or using ''' ''' once for multi line comment( The latter one consumes more memory so not a very preferred way)

# #  Q2. What are variables in Python? How do you declare and assign values to variables?

# # In Python, variables are used to store data values. They act as placeholders or containers for storing and referencing data within a program. Variables can hold various types of data, such as numbers, strings, lists etc.
# 
# # To declare and assign a value to a variable in Python, we use the assignment operator "=".

# # Q3. How do you convert one data type to another in Python?

# # Type casting can help convert one data type to another

# In[11]:


x = 12.78
y = int(x)


# In[12]:


print(y)


# # Q4. How do you write and execute a Python script from the command line?

# # Write a code in the IDE or text editor.save it in 'py' format 
# # Open the command prompt using windows CMD
# # redirect to the directory where the file is saved e.g. cd documents
# # Run python command. e.g. python assignment2.py
# 

# # Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[14]:


my_list = [1,2,3,4,5]

my_list[1:3]


# # Q6. What is a complex number in mathematics, and how is it represented in Python?

# # Complex number is something which has a real and an imaginary part. E.g : 34 + 17j

# In[17]:


a = 34 + 17j
type(a)


# # Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[18]:


age = 25


# In[19]:


print(age)


# # Q8 Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?

# In[20]:


price = 9.99
type(price)


# # Q9 Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?

# In[21]:


name = 'Kshitij Saxena'
print(name)


# In[22]:


type(name)


# # Q10. Given the string "Hello, World!", extract the substring "World".

# In[23]:


a = "Hello, World!"


# In[29]:


a[7:12]


# # Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.

# In[46]:


is_student = input("Are you currently a student? ")
if is_student == 'yes':
    print("Currently a student")
else:
    print("Not a student")


# In[44]:


is_student = True


# In[ ]:





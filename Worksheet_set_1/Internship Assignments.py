#!/usr/bin/env python
# coding: utf-8

# In[21]:


n=int(input("Enter Number Here "))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print("Factorial of the Number is", fact)


# In[6]:


n1=int(input("Enter the Number here "))
if n1>1:
    for i in range(2, n1):
        if (n1%i)==0:
            print(n1, "is not a Prime Number")
            break
    else:
        print(n1, "is a Prime Number")
elif n1==0 or 1:
    print(n1, "is not a Prime or Composite Number")
else:
    print(n1, "is a Composite Number")


# In[22]:


str1=str(input("Enter the word here= "))
rev_str1=reversed(str1)
if str1==rev_str1:
    print("The string is a Palindrome word")
else:
    print("The string is not a Palindrome word")


# In[35]:


import math
a=float(input("Enter base of the right sided triangle here= "))
b=float(input("Enter height of the right sided triangle here= "))
c=math.sqrt(a**2+b**2)
print("Third side of right sided triangle is = ", c)


# In[51]:


l=str(input("Enter Sentence here= "))
freq={}
for char in l:
    freq[char]=freq.get(char,0)+1
print(freq)


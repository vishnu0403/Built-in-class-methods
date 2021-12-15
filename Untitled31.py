#!/usr/bin/env python
# coding: utf-8

# In[7]:


class pow_x_n:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(pow_x_n().pow(2, -3));
print(pow_x_n().pow(3, 5));
print(pow_x_n().pow(100, 0));


# In[6]:





# In[ ]:





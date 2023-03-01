#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# ## Date:26/02/2023
# **Name:Mengyuan Li**

# Exercise 1:

# In[1]:


multiply = lambda a,b :a*b
multiply (5,6)


# Exercise 2:

# In[2]:


import math
radius = float(input("Radius: "))
area = math . pi * radius ** 2
print("Area of the circle is: ",area )


# Exercise 3:

# In[3]:


def calculate(num1, num2, operator):
    if operator == 'a':
        return num1 + num2
    elif operator == 's':
        return num1 - num2
    elif operator == 'm':
        return num1 * num2
    elif operator == 'd':
        return num1 / num2
    else:
        return "Invalid operator"

# Example usage
result = calculate(2, 5, 'd')
print(result)


# Exercise 4:

# In[4]:


class Rectangle(object):
    def __init__(self,length,width):
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w
r = Rectangle(5,10)
print(r.area())


# Exercise 5:

# In[5]:


class Shape:
    def __init__(self, name, length):
        self.name = name
        self.length = length
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name, length)
    
    def area(self):
        return self.length**2
    
    def describe(self):
        return f"This is a: {self.name}"
s = Square('square', 5)
print("The area is:", s.area())
print(s.describe())


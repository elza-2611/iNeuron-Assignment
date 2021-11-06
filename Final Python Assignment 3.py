# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:08:54 2021

@author: Elza Shany
"""

'''1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()'''

def myreduce(list1):
    print(sum(list1))
myreduce([1,2,3,4])

'''1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()'''
def myfilter(list1,ob):
    m=[]
    for i in list1:
        if i != ob:
            m.append(i)
        else:
            pass
    print(m)
myfilter([1,2,3],3)

'''2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists

['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
'''            
a=["x","y","z"]
b=[i*j for i in a for j in range(1,5)]
print(b)


'''['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] '''
a=['x','y','z']
c=[i*j for i in range(1,5) for j in a]
print(c)

'''[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''
a=(1,2,3)
d=[(j,i) for i in a for j in range(1,4)]
print(d)




















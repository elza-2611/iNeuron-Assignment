# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:44:47 2021

@author: Elza Shany
"""

#Python Basics Assignement
#1
'''1. Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed 
in a comma-separated sequence on a single line.'''
m=[]
for i in range(2000,3201):
    if i % 7==0 and i % 5 !=0:
        a=m.append(i)
print(m)

#2
'''2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.'''
first_name=input("Whats ur first name?")
last_name=input("Whats your last name?")
final_name= print(f"{last_name} {first_name}")

#3
'''3. Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3 '''
pi=3.14
d=12
r=d/2
r_3=r**3
v=1.3*pi*r_3
print(v)





        
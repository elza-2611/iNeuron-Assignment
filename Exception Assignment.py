# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 00:06:08 2021

@author: Elza Shany
"""


'''1. Write a function to compute 5/0 
and use try/except to catch the exceptions.'''
    
def five_zero(a):
    if a<0:
        raise Exception(a)
try:
    b=int(input("enter an integer "))
    a=int(input("enter an integer "))
    print(b/a)
    five_zero(a)
except Exception as e:
    print(e)

'''2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].'''

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for e in objects:
            print(i,j,e)


    
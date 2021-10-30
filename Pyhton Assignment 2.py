# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:34:20 2021

@author: Elza Shany
"""
#Python Assignment 2
#1
''' Create the below pattern using nested for loop in Python.'''
star=5
for i in range(0,star):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")
for i in range(star,0,-1):
    for j in range(0,i-1):
        print("*",end='')
    print("\r")
#2
'''2. Write a Python program to reverse a word after accepting the input from the user.
Input word: ineuron
Output: norueni'''

a=input("Name of organization:")
b=len(a)
print("Output Word: ",a[b::-1])






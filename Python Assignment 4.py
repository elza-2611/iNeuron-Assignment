# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:05:29 2021

@author: Elza Shany
"""

'''1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.'''
def filter_long_words(list1,num):
    for i in list1:
        if len(i)>num:
            print(i)
filter_long_words(["goa","mumbai","pune"],3)

'''2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.'''
def func(list1):
    m=[]
    for i in list1:
        n=len(i)
        m.append(n)
        print(m)
func(["goa","Maharashtra","Kerala"])

'''2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.'''
def vow(inputchar):
    if inputchar.lower()=="a" or inputchar.lower()=="e" or inputchar.lower()=="i" or inputchar.lower()=="o" or inputchar.lower()=="u" :
        print("True")
    else:
        print("False")
vow("z")































    
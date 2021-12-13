# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:43:55 2021

@author: vikas
"""

print?

help(print)


!pip install pandas


import pandas

import pandas as pd

print(pd.__version__)

!pip list


"Henry Harvin"
'Henry Harvin'
"Henry Harvin's"


print("Hello World")

print("hello world", "Welcome to Python")

print("hello world", "Welcome to Python", sep='---')

print("hello world", "Welcome to Python", "Welcome to Analytics",sep='---')

print("hello world", "Welcome to Python", sep='---')



print("hello world",  end='????')

print("Welcome to Python", end='?????')

print("Welcome to Analytics", sep='---')


print("I live in India")

country = "India"

type(country)

print("I live in", country)

print("I live in", country, sep="--")

print("I live in country")


print("I live in {0}".format(country))


lcountry = "India"
wcountry = "USA"

print("I live in {0} and Work in {1}".format(lcountry,wcountry))


lcountry = input("Enter Your Live Country->")
wcountry = input("Enter Your Work Country->")

print("I live in {0} and Work in {1}".format(lcountry,wcountry))

'''
int a;
a=10;
'''

a = 10
b= 10.3
c = "abc"
d =True


a = 10
b = 20

a+b

print("Value of a is {0}".format(a))


s1 = "Hello"
s2 = "World"

s1+s2

print (s1 + a)

print(s1 + str(a))


f = 10.2
f_i = int(f)
f_s = str(f)

i = 20
i_f = float(i)
i_s = str(i)

s = "233"
s_i = int(s)
s_f =float(s)


chr(100)
ord('a')
chr(64)



txt = "this course is @ based ^ on python (: and having good content"

t = ""

for i in txt:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)==32):
        t=t+i

t



















































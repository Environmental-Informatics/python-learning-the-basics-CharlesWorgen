#!/usr/bin/env python3
"""
2020/1/24
by Charles Huang

ThinkPython2e - Excercise 3.2
The function can accept two arguments (function and value), 
and call the assigned fucntion twice with the assigned value.

"""
# Sample of the exercise
def do_twice(f):
    f()
    f()
    
def print_spam():
    print('spam')
    
do_twice(print_spam)    

# Modify to take 1 function and 1 value, passing the value to function
def do_twice(f,v):
    f(v)
    f(v)
   
def print_twice(bruce): #Function from the chapter
    print(bruce)
    print(bruce)    
    
#Result
do_twice(print_twice,'spam')
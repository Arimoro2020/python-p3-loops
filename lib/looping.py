#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        if i == 1:
            print (i)
            print( "Happy New Year!")
            i -= 1
        else:
            print(i)
            i -= 1
        
        

    
    pass

def square_integers(int_list):
    int_list = [x ** 2 for x in int_list]
    return int_list

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
        if i > 0:
            print(f"{i}")
        elif i == 0:
            print("Happy New Year!")
        i -= 1
        # code goes here!
        pass
happy_new_year()

def square_integers(int_list):
    s = [h **2 for h in int_list]
    print(s)
    return s
    # code goes here!
    #pass
square_integers([1, 2, 3, 4, 5])
def fizzbuzz():
    for i in range(1, 101):
        if i% 3 == 0 and i %5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"{i}")
    # code goes here!
    pass
fizzbuzz()
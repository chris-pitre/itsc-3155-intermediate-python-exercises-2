# Chris Pitre
# Intermediate Python Exercises 2
# Exercise 2

import random
import time

num = random.randint(15, 35)

def fib(num):
    """
    Recursive function that returns the nth number in the fibonacci sequence

    Parameters
    ----------
    num : int
        nth number to be returned in the fibonacci sequence
    
    Returns
    -------
    int
        nth number in the fibonacci sequence
    """
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

start_time = time.time()
fibnum = fib(num)
exec_time = time.time() - start_time

print(f"fib({num})={fibnum}")
print(f"fib({num}) took {exec_time} seconds")

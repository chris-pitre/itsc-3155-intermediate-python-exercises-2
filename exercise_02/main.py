import random
import time

num = random.randint(15, 35)

def fib(num):
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

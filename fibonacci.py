from functools import lru_cache

def fibonacci(n):
    # test how many times the function is called
    print('fibonacci called with n= ', n)
    # ends up repeating itself a LOT
    # bc it calculates the fibonacci of EVERY lesser number FOR every lesser number!
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=None)
def fibonacci_optimized(n):
    # test how many times the function is called
    print('fibonacci_optimized called with n= ', n)
    # ends up repeating itself a LOT
    # bc it calculates the fibonacci of EVERY lesser number FOR every lesser number!
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fibonacci_optimized(n-1) + fibonacci_optimized(n-2)
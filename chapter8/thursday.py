# writing a factorial using recursive fuctions
# many times i did that
# writing the recursive fibonacci sequence
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))
# using memoization with fibonacci sequence
# cache = {}  # used to cache values to be used later
# def fib1(n):
#     if n in cache:
#         return cache[n]
#     result = 0
#     # base case
#     if n<= 1:
#         result = n
#     else:
#         return fib1(n-1)+fib1(n-2)
#     cache[n] = result  # save result into dictionary with n as the key
#     return result
# print(fib1(50))

# using @lru_cache, python's default moization/caching technique
from functools import lru_cache
@lru_cache()  # python's default moization/caching system
def fib2(n):
    if n<=1:
        return n
    else:
        return fib2(n-1)+fib2(n-2)

print(fib2(50))
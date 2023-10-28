#  using lamda to square a number
print((lambda x : x**2)(4)) #  takes in 4 and returns the number squared
#  passing multiple arguments
mul = lambda x,y : x*y
print(mul)
result = mul(10,5)
print(result)
#  using if/else within a lambda to return the greater number
greater = lambda x,y : x if x>y else y
result1 = greater(20,54)
print(result1)
#  Returning a lambda
def my_func(n):
    return lambda x: x*n
doubler = my_func(2) # returns equivalent of lambda x: x*2
print(doubler(5))
tripler = my_func(3) # returns equivalent of lambda x : x*3
print(tripler(5))

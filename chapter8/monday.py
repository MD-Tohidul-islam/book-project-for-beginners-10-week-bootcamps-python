l = [x  for x in range(10)]
print(l)
nums = [x for x in range(10) if x% 2 == 0] # generates a lost of even number up to 10
print(nums)
nums2 = ['even ' if x%2 ==0 else 'odd' for x in range(10)]
print(nums2)
numbers = [2,4,6,8]
squared_nums = [num**2 for num in numbers]
print(squared_nums)
numbers1 = [x for x in range(10)]
squares = {num: num**2 for num in numbers if num%2==0}
print(squares)
#  monday exercises
#  Degree conversion: using list comprehension, cov=nvert the following list to Fahrenheit. currently the degrees are in celsius tem.
#  the formula is (9/5)*c +32
degree = [12,21,15,32]
fahrenheit_temp = [round(((9/5)*c +32),1) for c in degree]
print(fahrenheit_temp)
nums3 = [i for i in range(1,101) if i%25 == 0]
print(nums3)
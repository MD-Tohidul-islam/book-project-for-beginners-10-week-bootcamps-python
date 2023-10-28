#  using the map function without lambdas
def convertDeg(c):
    return round((9/5)*c + 32,2)
temps = [12.5,13.6,15,9.2]
convert_temps = map(convertDeg,temps) #  return map object
print(convert_temps)
convert_temps = list(convert_temps) #  type convert map object
# into list of covert temps
print(convert_temps)

#  Map with lambdas
#  using a map function with lambdas
temps1 = [12.5,13.6,15,9.2]
convert_temps1 = list(map(lambda c:round((9/5)*c + 32,2),temps1))
print(convert_temps1)

#  using the dilter function without lambda
def filterTemps(c):
    converted = (9/5)*c + 32
    return True if converted>55 else False
temps2 = [12.5,13.6,15,9.2]
filter_temps = filter(filterTemps,temps2)
print(filter_temps)
filter_temps = list(filter_temps)
print(filter_temps)
# using the filter function with lambda functions, filter out temps below 55F
temps = [ 12.5, 13.6, 15, 9.2 ]
filtered_temps = list( filter( lambda C : True if (9/5) * C + 32 > 55 else
False, temps) ) # type convert the filter
print(filtered_temps)
print()
def convertDeg(degrees):
    filtered = [ ]
    for degree in degrees:
        result = (9/5) * degree + 32
        if result > 55:
            filtered.append(degree)
    return filtered
temps = [ 12.5, 13.6, 15, 9.2 ]
filtered_temps = convertDeg(temps)
print(filtered_temps)
#  using Reduce
#  for informationn putposes this is how you use the reduce function
from functools import reduce
nums = [1,2,3,4]
result = reduce(lambda a,b: a*b,nums) # result is 24
print(result)
names = ['ryan','PAUL','kevin connors']
name = list(map(lambda x:x.title(),names))
print(name)
names = [ "Amanda", "Frank", "abby", "Ripal", "Adam" ]
filter_name = list(filter(lambda c:True if c[0].upper() != 'A' else False,names))
print(filter_name)



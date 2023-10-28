#  frozensets are essentially the combination of a set and a tuple.
#  they are immutable, unordered and unique
fset = frozenset([1,2,3,4])
print(type(fset))


import csv
with open('test.csv',mode = 'w',newline = '') as f:
    writer = csv.writer(f,delimiter = ',')
    writer.writerow(['name','city'])
    writer.writerow(['craig lou','taiwan'])
with open('test.csv','r') as file:
    reader = csv.reader(file,delimiter = ',')
    for row in reader:
        print(row)
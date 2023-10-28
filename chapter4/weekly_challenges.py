# 1. pyramids: use a for loop to build a pyramid of x's
#     it should be modular so that if you loop to 5 or 50, it still creates evenly spaced
# row . Hint: Multiply the string 'x' by the row. for cxample , if you loop to the range of 4,
# it should produce the following result:

rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
size = 7
m = (2*size) - 1
for i in range(0,size):
    for  j in range(m):
        print(end=' ')
    m = m-1
    for j in range(0,i+1):
        print('*',end=' ')
    print(' ')

# 2 output names : write a loop that will iterate over a list of items
#  and only output items which have letter inside of a string
names = ['john',' ','amanda',5]
new_names= []
for i in names:
    if isinstance(i,str):
        if i.isalpha():
            new_names.append(i)
print(new_names)
# 3 convert celsius: given a list of tempreatures that are in celsius,
# write a loop that iterates over the list and output the temperature converted int
# fahrenheit.
temp = [32,12,44,29]
fahrenheit_temp = []
for i in temp:
    f = (9/5)*i+32
    fahrenheit_temp.append(f)
print(fahrenheit_temp)


a,c = 'bo','bob'
b = a
print(hash(a),hash(b),hash(c))
#  creating data collections to rest for time complexity
import time
d = {} # generate fake dictionary
for i in range(1000000):
    d[i] = 'value'
big_list = [x for x in range(1000000)] # generate fake list
#  retrieving information and tracking time to see which is faster
start_time = time.time() # tracking time for dictionary
if 99999 in d:
    print('Found in dictionary')
end_time = time.time()
print('Elapsed time for dictionary:{}'.format(end_time-start_time))
start_time = time.time()
if 99999 in big_list:
    print('Found in list')
end_time = time.time()
print('Elapsed time for list: ',end_time-start_time)
#  testing bubble sort vs. insertion sort
def bubblesort(a_list):
    for i in range(len(a_list)):
        switched = False
        for j in range(len(a_list)-1):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j-1] = a_list[j-1],a_list[j]
                switched = time
        if switched == False:
            break
    return a_list
def insertionsort(alist):
    for i in range(1,len(alist)):
        if alist[i]<alist[i-1]:
            for j in range (i,0,-1):
                if alist[j]< alist[j-1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]
        else:
            break
    return alist
#  calling bubble sort and insertion sort to test time complexity
from random import randint
nums = [randint(0,100) for x in range(5000)]
start_time = time.time()
bubblesort(nums)
end_time = time.time()-start_time
print('Elasped time for bubble sort:',end_time)
start_time = time.time()
insertionsort(nums)
end_time = time.time()-start_time
print('Elapsed time for insertion sort: ',end_time)





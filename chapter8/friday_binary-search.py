#  setting up import and generating a list of random numbers to work with
import random
nums = [random.randint(0,20) for i in range(10)]
#  print(sorted(nums))
def binary_search(a_list,num):
    a_list.sort()
    while a_list:
        mid = len(a_list)//2
        if a_list[mid] == num:
            return True
        elif a_list[mid]>num:
            a_list = a_list[:mid]
            # print(a_list)
        elif a_list[mid]<num:
            a_list = a_list[mid+1:]
            # print(a_list)
    return False


print(sorted(nums))  # for debugging purposes
print(binary_search(nums,3))

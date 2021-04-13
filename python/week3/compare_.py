import sys
sys.path.insert(0,'/Users/apple/MachineLearning/python')
from function_python.compare_array import compare_arr
arr1,arr2=[],[]
len_arr = 0
len_arr1 = input('First array length:')
len_arr2 = input('\nSecond array length:')
for number in range(0,int(len_arr1)):
    input_arr = input('arr1[{}]='.format(number))
    arr1.append(int(input_arr))
    del input_arr
for number in range(0,int(len_arr2)):
    input_arr = input('arr2[{}]='.format(number))
    arr2.append(int(input_arr))
    del input_arr
compare_arr(arr1,arr2)
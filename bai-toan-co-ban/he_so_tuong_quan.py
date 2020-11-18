from collections import Counter
import requests
from PIL import Image
from io import BytesIO
arr = [1,2,3,4,5]
arr1 =[1,2,3,4,5]
def varian(arr):
    sum_arr=sum(arr)
    len_arr=len(arr)
    var = sum_arr/len_arr
    arr_var = []
    for i in arr:
        arr_var.append((i-var)**2)
    sum_arr_var=sum(arr_var)
    return sum_arr_var/len_arr
def sub_arr(arr,medium_arr):
    for i in range(len(arr)):
        arr[i] -= medium_arr
    return arr 
def he_so_tuong_quan(arr, arr1):
    len_arr = len(arr)
    len_arr1 = len(arr1)
    medium_arr = sum(arr)/ len_arr
    medium_arr1 = sum(arr1)/ len_arr1
    arr = sub_arr(arr,medium_arr)
    arr1 = sub_arr(arr1,medium_arr1)
    arr_arr1 = []
    for x,y in zip(arr,arr1):
        arr_arr1.append(x*y)
    medium_arr_arr1 = sum(arr_arr1)/ len_arr
    return medium_arr_arr1
print("He so tuong quan arr va arr1:", he_so_tuong_quan(arr,arr1)/((varian(arr)*varian(arr1))**0.5))
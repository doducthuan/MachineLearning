import numpy as np
from PIL import Image
from io import BytesIO
import requests
ima1 = requests.get('https://www.dropbox.com/s/vfe090qo24t3v46/img1.png?raw=1')
ima2 = requests.get('https://www.dropbox.com/s/vtz8ik7mb1e1is7/img2.png?raw=1')
ima3 = requests.get('https://www.dropbox.com/s/auxezlf6ijoejwo/img3.png?raw=1')
ima4 = requests.get('https://www.dropbox.com/s/w5oc29l57f77arp/img4.png?raw=1')
image1 = Image.open(BytesIO(ima1.content))
image2 = Image.open(BytesIO(ima2.content))
image3 = Image.open(BytesIO(ima3.content))
image4 = Image.open(BytesIO(ima4.content))
image1_array = np.asarray(image1).flatten().tolist()
image2_array = np.asarray(image2).flatten().tolist()
image3_array = np.asarray(image3).flatten().tolist()
image4_array = np.asarray(image4).flatten().tolist()
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
def find_corr_x_y(arr, arr1):
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
    return medium_arr_arr1/((varian(arr)*varian(arr1))**0.5)
corr_1_2 = find_corr_x_y(image1_array,image2_array)
corr_1_3 = find_corr_x_y(image1_array,image3_array)
corr_1_4 = find_corr_x_y(image1_array,image4_array)
corr_3_4 = find_corr_x_y(image3_array,image4_array)
print("corr_1_2:",corr_1_2)
print("corr_1_3:",corr_1_3)
print("corr_1_4:",corr_1_4)
print("corr_3_4:",corr_3_4)

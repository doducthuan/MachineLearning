def min(arr):
    value_min = arr[0]
    for value_arr in arr:
        if(value_arr <= value_min):
            value_min = value_arr
    return value_min
def max(arr):
    value_max = arr[0]
    for value_arr in arr:
        if(value_arr >= value_max):
            value_max = value_arr
    return value_max
def mean(arr):
    sum_arr = 0
    for value in arr:
        sum_arr += value
    return sum_arr/len(arr)
def standard_deviation(arr):
    arr_mean = []
    for value in arr:
        arr_mean.append((value-mean(arr))**2)
    sum_arr_mean = 0
    for value in arr_mean:
        sum_arr_mean += value
    return sum_arr_mean/len(arr_mean)
arr_sepal_length = []
arr_sepal_width = []
arr_petal_length = []
arr_petal_width = []
line = 0
with open('text1.txt','r') as arr_all:
    for i in arr_all:
        if(line > 0):
            arr = i.split(',')
            arr_sepal_length.append(float(arr[1].strip()))
            arr_sepal_width.append(float(arr[2].strip()))
            arr_petal_length.append(float(arr[3].strip()))
            arr_petal_width.append(float(arr[4].strip()))
        line += 1
print("SepalLength: Max_Value:{:<5g}, Min_Value:{:<5g}, Mean:{:<5g}, Standard_deviation:{:<5g}".format(max(arr_sepal_length),min(arr_sepal_length),mean(arr_sepal_length),standard_deviation(arr_sepal_length)))
print("SepalWidth : Max_Value:{:<5g}, Min_Value:{:<5g}, Mean:{:<5g}, Standard_deviation:{:<5g}".format(max(arr_sepal_width),min(arr_sepal_width),mean(arr_sepal_width),standard_deviation(arr_sepal_width)))
print("PetalLength: Max_Value:{:<5g}, Min_Value:{:<5g}, Mean:{:<5g}, Standard_deviation:{:<5g}".format(max(arr_petal_length),min(arr_petal_length),mean(arr_petal_length),standard_deviation(arr_petal_length)))
print("SepalLength: Max_Value:{:<5g}, Min_Value:{:<5g}, Mean:{:<5g}, Standard_deviation:{:<5g}".format(max(arr_petal_width),min(arr_petal_width),mean(arr_petal_width),standard_deviation(arr_petal_width)))
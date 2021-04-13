def big_arr(*num):
    big_of_arr =0
    for element in num:
        if big_of_arr <= element:
            big_of_arr = element
    return big_of_arr
num = [1,2,3,4,5]
print('Value max of array is: {}'.format(big_arr(*num)))
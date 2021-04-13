def sum_arr(*input_array):
    total = 0
    for index in range(0,len(input_array)):
        total += input_array[index]
    return total
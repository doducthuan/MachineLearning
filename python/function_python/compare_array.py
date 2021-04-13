def compare_arr(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    count=0
    if len_arr1 != len_arr2:
        print('Two array different')
    else:
        for number in range(0,len_arr1):
            if arr1[number] == arr2[number]:
                count +=1
            else:
                print('Two array different')
                break
        if count == len_arr1:
            print('Two array same')

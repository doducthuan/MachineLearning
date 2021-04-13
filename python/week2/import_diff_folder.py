import sys
sys.path.insert(0,'/Users/apple/MachineLearning/python')
from week1.big_array import big_arr
arr = [1,2,3,4,5]
big = big_arr(*arr)
print(big)
from week2.test_folder.print_name import pri_name
name = 'Sir'
pri_name(name)
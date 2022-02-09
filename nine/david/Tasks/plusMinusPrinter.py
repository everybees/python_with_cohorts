#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(userNum):
    # Write your code here
    total_positive = 0.0
    total_negative = 0.0
    total_zeros = 0.0
    
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0
    
    for num in userNum:
        if num > 0:
            positive_counter += 1
        elif num < 0:
            negative_counter += 1
        elif num == 0:
            zero_counter += 1
            
    total_positive = positive_counter/len(userNum)
    print(round(total_positive, 6))
    print()
    
    total_negative = negative_counter/len(userNum)
    print(round(total_negative, 6))
    print()
    
    total_zeros = zero_counter/len(userNum)
    print(round(total_zeros, 6))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

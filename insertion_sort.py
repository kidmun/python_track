#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    j = n - 1
    cur = arr[j]
    while j > 0 and cur < arr[j - 1]:
        arr[j] = arr[j-1]
        copy = [str(x) for x in arr]
        print(" ".join(copy))
        j -= 1
    arr[j] = cur
    arr = [str(x) for x in arr]
    print(" ".join(arr))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

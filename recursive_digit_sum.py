#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    n = [int(x) for x in n]
    n = sum(n)
    n = str(n)
    n = n * k
    def recu(s):
        val = 0
        for i in range(len(s)):
            val += int(s[i])
        return str(val)
 
    while len(n) > 1:
        n = recu(n)

    
    return int(n[0])
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') # while len(n) > 1:
    #     n = list(str(recu(n))

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

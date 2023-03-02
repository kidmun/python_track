
import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    count = Counter()
 
    for query in queries:
    
        count[query[0]] += query[2]
        count[query[1] + 1] -= query[2]
    cur = 0
    lar = 0
    for num in sorted(count):
        if num in count:
            cur += count[num]
        lar = max(lar, cur)
    return lar
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

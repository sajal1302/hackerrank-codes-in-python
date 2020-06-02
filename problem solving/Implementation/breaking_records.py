#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    a=b=0
    min=max=scores[0]
    
    for i in scores[1:]:
        
              
        if i>max:
            max = i
            a=a+1
        if i<min:

            min=i
            b=b+1

    return a,b
        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

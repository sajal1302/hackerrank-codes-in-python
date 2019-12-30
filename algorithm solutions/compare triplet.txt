#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    k=len(a)
    z=0
    y=0
    for i in range (0,k):
        
        if(a[i]>b[i]):
            z=z+1
        if(a[i]<b[i]):
            y=y+1
        if(a[i]==b[i]):
            pass
    return z,y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

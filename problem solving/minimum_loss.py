#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    x=sorted(price)
    ml=10**10
    for i in range(1,len(price)):
        if x[i]-x[i-1]<ml and price.index(x[i])<price.index(x[i-1]):
            
            ml=x[i]-x[i-1]
    
    return ml

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
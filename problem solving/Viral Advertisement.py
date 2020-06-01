#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared=5
    cumlative=0
    for i in range(0,n):
        liked=math.floor(shared/2)
        cumlative=liked+cumlative
        shared=liked*3
        
    return cumlative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

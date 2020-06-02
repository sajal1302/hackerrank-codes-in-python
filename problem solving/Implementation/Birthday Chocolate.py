#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
        c=0
        
       
        k=len(s)
        for i in range(0,k-m+1):
            n=0
            a=0
            while n!=m:
                a=a+s[i+n]
                n=n+1
            if a==d:
                c=c+1
            else :
                continue
                    
        return c



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

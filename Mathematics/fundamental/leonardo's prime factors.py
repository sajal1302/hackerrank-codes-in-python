#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    prime_number=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
    c=0
    t=1
    while t < n:
        t =t* prime_number[c]
        if t > n:
            break
        c= c+1
    return c

    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()

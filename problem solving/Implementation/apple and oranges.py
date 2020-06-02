#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    z=[]
    y=[]
    c=0
    p=0
    for i in apples:
        z.append(i+a)
    for j in oranges:
        y.append(j+b)
   #print(z)
    
    for j in z:
        #print(j,s,t)
        if(j>=s and j<=t):
            
            c=c+1
        else:
            continue
    for k in y:
        if k>=s and k<=t:
            p=p+1
    print(c)
    print(p)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
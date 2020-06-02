#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
   if((x2 > x1 and v2 >= v1) or ((x1-x2) % (v2-v1)) != 0):
       return 'NO'

   else:
       return 'YES'

''' after how many jumps(y) will they meet :
x1+v1*y=x2+v2*y
y= x1-x2/v2-v1
if remainder of above division is zero it means we can get a wholeno. y which means after specific jumps  both kangroo can meets '''


        
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

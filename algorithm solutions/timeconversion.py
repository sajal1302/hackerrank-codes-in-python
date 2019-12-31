#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    a = s[8:]
    h = int(s[0:2])
    if a == 'PM':
            if h ==12:
                return(s[0:8])
            else:
                h = h + 12
                return(str(h)+s[2:8])
    elif (h == 12):
        return('00'+s[2:8])
    else:
        return(s[0:8])
    
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

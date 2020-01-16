#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    '''ly=[31,60,91,121,152,182,213,244,274,305,335,366]
    y= [31,59,90,120,151,181,212,243,273,304,334,365]
    if 1700<=year<=1917:
        
    if  1917< year<=2700:'''
    
    if year<=1917 and year %4==0:
         return '12.09.%s' %year 

    if year ==1918:
        return '26.09.1918'

    if  year>=1919 and ((year%400==0 or (year %4==0 and year%100 !=0))):
        return '12.09.%s' %year 
    else:
        return '13.09.%s' %year
'''((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):'''
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

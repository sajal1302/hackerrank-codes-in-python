#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n%2 != 0):
    print("Weird")
elif (2<n<5 and n%2==0):
    print("Not Weird")
elif(n in range (6, 21) and n % 2 == 0 ):
    print("Weird")
elif(n>20 and n%2==0 ):
    print("Not Weird")
else:
    pass

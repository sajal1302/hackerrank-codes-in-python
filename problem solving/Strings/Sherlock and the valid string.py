#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    c = Counter(s)
    f = Counter(c.values())
    if len(f) == 1:
        return "YES"
    elif len(f) == 2:
        ma = max(f.keys())
        mi = min(f.keys())
        if ma -mi == 1 and f[ma] == 1:
            return "YES"
        elif mi == 1 and f[mi] == 1:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

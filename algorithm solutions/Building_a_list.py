

import os
import sys
from itertools import combinations

# Complete the solve function below.
def solve(s):
    w=[]
    i=1
    j2=[character for character in s]
    while i<=len(s):
        w+=map(''.join,combinations(j2,i))
        i+=1
    return sorted(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = input()

        result = solve(s)

        fptr.write('\n'.join(result))
        fptr.write('\n')

    fptr.close()
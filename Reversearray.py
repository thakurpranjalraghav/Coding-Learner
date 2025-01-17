#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(arr):
    return arr[::-1]   

 
n = int(input())

 
arr = list(map(int, input().split()))

 
reversed_arr = reverseArray(arr)

 
print(*reversed_arr)

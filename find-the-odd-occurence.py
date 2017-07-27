# Problem
# --------
# Find the Odd Occurence
#
# Description
# --------------
# Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number.
#
# Expected Time Complexity: O(n)
# Expected Auxiliary Space​: Constant
#
# Input:
#
# The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines.
#
# The first line of each test case consists of an integer N, where N is the size of array.
# The second line of each test case contains N space separated integers denoting array elements.
#
# Output:
#
# Corresponding to each test case, print in a new line, the number which occur odd number of times.
#
# Constraints:
#
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 202
# 1 ≤ A[i] ≤ 1000
#
# Example:
#
# Input
# 1
# 5
# 8 4 4 8 23
#
# Output
# 23

t = int(input())
listSize = [0] * t
listData  = [0] * t

for i in range(t):
    listSize[i] = int(input())
    listData[i] = list(map(int, input().split()))
    result = {}
    find = 0
    for j in range(listSize[i]):
        result[str(listData[i][j])] = int(result.get(str(listData[i][j]),0)) + 1

    for	k, v in result.items():
        if(int(v) % 2 != 0 ):
            print(k)

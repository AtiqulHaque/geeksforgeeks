# Problem : Missing number in array
#
#
# Description :
#
# Given an array of size n-1 and given that there are numbers from 1 to n with one missing,
# the missing number is to be found.
#
# Input:
#
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N,size of array.
# The second line of each test case contains N-1 input C[i],numbers in array.
#
# Output:
#
# Print the missing number in array.
#
# Constraints:
#
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000
# 1 ≤ C[i] ≤ 1000
#
# Example:
#
# Input
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10
#
# Output
# 4
# 9


t = int(input())
listSize = [0] * t
listData  = [0] * t

for i in range(t):
    listSize[i] = int(input())
    listData[i] = list(map(int, input().split()))
    result = [0] * listSize[i]
    for j in range(len(listData[i])):
        result[listData[i][j] - 1] = listData[i][j]

    for j in range(len(result)):
        if(result[j] == 0 ):
            print (j + 1)

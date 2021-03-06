# Elements in the Range
#
# An array containing positive elements is given. ‘A’ and ‘B’ are two numbers defining a range.
# Write a function to check if the array contains all elements in the given range.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case
# contains space separated integers n, A and B which denotes the number of
# elements in the array a[] and the range [A, B].
# Next line contains space separated n elements in the array a[].
#
# Output:
# Print "Yes" if all the elements in the range are present else print "No".
#
# Constraints:
# 1<=T<=100
# 1<=n<=1000
# 1<= A < B<=1000
# 1<=a[i]<=1000​
#
# Example:
# Input:
# 1
# 7 2 5
# 1 4 5 2 7 8 3
#
# Output:
# Yes


t = int(input())
rangeData = [0] * t
testData  = [0] * t

for i in range(t):
    rangeData[i] = list(map(str, input().split()))
    testData[i] = list(map(str, input().split()))

    length = rangeData[i][0]
    rangeA = rangeData[i][1]
    rangeB = rangeData[i][2]
    found = True

    for j in range(int(rangeA) ,int(rangeB)):
        if(str(j) not in testData[i] ):
            found = False
            break


    if(found):
        print("Yes")
    else:
        print ("No")

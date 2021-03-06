"""
Given an integer N, recursively sum digits of N until we get a single digit.  The process can be described below

If N < 10
    digSum(N) = N
Else
    digSum(N) = Sum(digSum(N))
Example:

Input : 1234
Output : 1
Explanation : The sum of 1+2+3+4 = 10,
              digSum(x) == 10
              Hence ans will be 1+0 = 1
Input:

The first line contains an integer T, total number of test cases. Then following T lines contains an integer N.

Output:

Repeated sum of digits of N.

Constraints:

1 ≤ T ≤ 100

1 ≤ N ≤ 1000000

Example:

Input
2
123
9999

Output
6
9
"""

def sumOfDigit(d):

    if (d < 10):
        return d

    d = list(str(d))
    r = 0
    for i in d:
        r += int(i)

    return sumOfDigit(r)

inputlist = []
t = int(raw_input())

while t:
    inputlist.append(int(raw_input()))
    t = t-1

for i in range(0, len(inputlist)):
    print sumOfDigit(inputlist[i])

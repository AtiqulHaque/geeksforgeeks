"""
Given a number N, print all its unique prime factors in increasing order.

Input : N = 100
Output: 2 5

Input : N = 35
Output: 5 7
Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:
Print all prime factors in increasing order.

Constraints:
1 ≤ T ≤ 200
2 ≤ N ≤ 10000

Example:
Input:
2
100
35

Output:
2 5
5 7
"""


"""Count divisor check."""
import math


def isPrime(n):
    for i in range(0, int(math.ceil(math.sqrt(n + 1)))):
        if(i == 1 or i == 0):
            continue
        if(n % i == 0):
            return False
        else:
            continue

    return True


def countDivisor(n):
    for i in range(1, n + 1):
        if(i == 1):
            continue
        if(n % i == 0):
            if(isPrime(i)):
                print i,

inputlist = []
t = int(raw_input())

while t:
    inputlist.append(int(raw_input()))
    t = t-1

for i in range(0, len(inputlist)):
    countDivisor(inputlist[i])
    print ""

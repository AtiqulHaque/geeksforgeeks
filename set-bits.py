"""
Given a positive integer N, print count of set bits in it. For example, if the given number is 6, output should be 2 as there are two set bits in it.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The next T lines will contain an integer N.

Output:
Corresponding to each test case, in a new line, print count of set bits in it.

Constraints:

1 ≤ T ≤ 100

1 ≤ N ≤ 1000000


Example:

Input:

2
6
11


Output:
2
3
"""

"""Check set bit funtion."""


def CountSetBits(number):
    """Check set bit funtion."""
    bits = list(bin(number).lstrip('-0b'))
    setBits = 0
    for i in range(len(bits)):
        if(int(bits[i]) == 1):
            setBits = setBits + 1

    return setBits

inputString = []
t = int(raw_input())

while t:
    inputString.append(raw_input())
    t = t-1

for i in range(0, len(inputString)):
    print CountSetBits(int(inputString[i]))

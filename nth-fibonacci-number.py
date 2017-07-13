"""
Given a positive integer N, find the Nth fibonacci number. Since the answer can be very large, print the answer modulo 1000000007.

Input:

The first line of input contains T denoting the number of testcases.Then each of the T lines contains a single positive integer N.

Output:

Output the Nth fibonacci number.

Constraints:

1<=T<=200
1<=N<=1000

Example:

Input:
3
1
2
5

Output:
1
1
5
"""


def febonacci(limit, loop=3, previous=0, current=1):

    if(loop > limit):
        return current

    return febonacci(limit, loop + 1, current, previous + current)


inputlist = []
t = int(raw_input())

while t:
    inputlist.append(int(raw_input()))
    t = t-1

for i in range(0, len(inputlist)):
    z = febonacci(inputlist[i])
    print z % 1000000007

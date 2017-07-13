"""
Given a value N, you need to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

Input :
The first line contains integer T, denoting number of test cases. Then T test cases follow. The only line of each test case contains an integer N.

Output :
Print in a new line the answer of each test case .

Constraints :

1<=T<=10^5
1<=N<=10^9

Example:
Input :
3
6
10
30

Output :
1
2
3
"""


"""Count divisor check."""
import math


def isPrime(n):
    """Determind" number is prime or not prime."""
    for i in range(0, int(math.ceil(math.sqrt(n + 1)))):
        if(i == 1 or i == 0):
            continue
        if(n % i == 0):
            return False

    return True


def numberOfDivisor(n):
    """Find 3 divisor from a given number."""
    count = 0
    for i in range(2, n+1):
        number = math.sqrt(i)
        # print number
        if(number.is_integer()):
            if(isPrime(number)):
                count += 1
        else:
            continue

    return count

# Start form here

# Input list for
inputlist = []

# Get test case from user
t = int(raw_input())

while t:
    inputlist.append(int(raw_input()))
    t = t-1

for i in range(0, len(inputlist)):
    print numberOfDivisor(inputlist[i])

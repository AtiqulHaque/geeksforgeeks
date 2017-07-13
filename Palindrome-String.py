"""
Given a string s check if it is palindrome or not.

Input:
The first line contains 'T' denoting the number of test cases. Then follows description of test cases.
Each case begins with a single integer N denoting the length of string. The next line contains the string s.


Output:
Print "Yes" if it is a palindrome else "No". (Without the double quotes)


Constraints:
1<=T<=30
1<=N<=100


Example:
Input:
1
4
abba

Output:
Yes
"""

"""Palindrom word check funtion."""


def Palindrom(text):
    """Palindrom word check funtion."""
    text = list(text)
    count = len(text)

    for i in range(count):
        if(text[i] == text[(count-i) - (count + 1)]):
            continue
        else:
            return "No"

    return "Yes"


inputLength = []
inputString = []
t = int(raw_input())

while t:
    inputLength.append(int(raw_input()))
    inputString.append(raw_input())
    t = t-1

for i in range(0, len(inputString)):
    print Palindrom(inputString[i].strip())

import math
# Input number of test cases
t = int(input())
stData = [0] * t
nith = [0] * t
for i in range(t):
    nith[i] = int(input())
    stData[i] = list(map(str, input().split()))
print(nith,stData)

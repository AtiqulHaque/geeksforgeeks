import math
t = int(input())
inputData = [0] * t
for i in range(t):
    inputData[i] = list(map(float, input().split()))
    result = (6 * inputData[i][1]) - (30 * int(inputData[i][0]) + (.5 * inputData[i][1]))
    if(result < 0):
        result = (result * -1)
    if(result > 180):
        print (math.floor(360 - result))
    else:
        print (math.floor(result))

t = int(input())
inputData = [0] * t

for i in range(t):
    inputData[i] = int(input())
    if((inputData[i] & (inputData[i] -1) == 0)  and inputData[i] != 0):
        print("YES")
    else:
        print("NO")

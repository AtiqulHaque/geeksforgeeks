
#code
t = int(input())

for i in range(t):
    iData = list(map(str, input().split()))
    outData = [0] * (len(iData) -1)
    for i in range(len(iData) -1):
        j = i
        limit = len(iData) - 1

        while True:
            if j >= limit:
                outData[i] = -1
                break
            elif iData[j] > iData[j+1]:
                outData[i] = iData[j]
                break
            else:
                j += 1
        
    print(outData)

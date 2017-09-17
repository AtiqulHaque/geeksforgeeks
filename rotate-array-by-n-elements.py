t = int(input())
ins = [0] * t
inputData = [0] * t
for i in range(t):
    ins[i] = list(map(int, input().split()))
    inputData[i] = list(map(int, input().split()))
    Output = inputData[i][(ins[i][1]):(ins[i][0])] + inputData[i][0:(ins[i][1])]
    for j in Output:
        print(j,end=' ')
    print('')

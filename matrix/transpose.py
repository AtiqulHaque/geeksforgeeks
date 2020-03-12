for _ in range(int(input())):
    n = int(input())
    iData = list(map(int,input().split(' ')))
    inAray = []
    inArayT = []

    for i in range(n):
        inAray.append(iData[i * n : (n * i) + n])
        inArayT.append([0] * n)
    
    for i in range(n):
        for j in range(n):
            inArayT[j][i] = inAray[i][j]
    
    for i in range(n):
        for j in range(n):
            print(inArayT[i][j],end=' ')
    print('')

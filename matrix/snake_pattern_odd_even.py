for _ in range(int(input())):
    n = int(input())
    iData = list(map(int,input().split(' ')))
    inAray = []

    for i in range(n):
        inAray.append(iData[i * n : (n * i) + n])
    

    totalRow = len(inAray) - 1
    currentRow = 0
    currentRowType = "even"
    while currentRow <= totalRow:
        if currentRowType == 'even':
            for i in inAray[currentRow]:
                print(i,end=" ")
            currentRow += 1
            currentRowType = "odd"
        elif currentRowType == 'odd':
            for i in inAray[currentRow][::-1]:
                print(i, end=" ")
            currentRow += 1
            currentRowType = "even"
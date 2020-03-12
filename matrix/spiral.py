for _ in range(int(input())):
    n = int(input())
    iData = list(map(int,input().split(' ')))
    inAray = []

    for i in range(n):
        inAray.append(iData[i * n : (n * i) + n])
    
    
    
    directions = [
        'left-right',
        'top-bottom',
        'right-left',
        'bottom-top'
    ]
    start = 0
    end = 0

    for i in directions:
        if i == 'left-right':
            while end < n:
                print(inAray[start][end],end=" ")
                end += 1
            start = 1
            end = n -1 
        elif i == 'top-bottom':
            while start < n:
                print(inAray[start][end],end=" ")
                start += 1
            start = n -1 
            end = n - 2
        elif i == 'right-left':
            while end > 0:
                print(inAray[start][end],end=" ")
                end -= 1
        else:
            start = n - 1
            end = 0
            while start > 0:
                print(inAray[start][end],end=" ")
                start -= 1
            
    
    print("")
    for i in range(n):    
        print(inAray[i])
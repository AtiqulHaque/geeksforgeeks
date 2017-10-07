def allFillByZero(r):
    for i in r:
        if(i == 0):
            return True
    return False

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while (allFillByZero(a)):
        count += 1
        for i in range(n):
            if(a[i] == 1):
                prev = i -1
                nexts = i + 1
                if(prev >= 0):
                    if(a[prev] == 0):
                        a[prev] = 1
                if(nexts <= (n - 1)):
                    if(a[nexts] == 0):
                        a[nexts] = 1
    print(count)

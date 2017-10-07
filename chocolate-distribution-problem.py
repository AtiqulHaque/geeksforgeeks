for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    a.sort()
    r = 10000000
    for i in range(n):
        t = n - ((i + m) - 1)
        if(t == 0):break
        v = a[(i + m)-1] - a[i]
        if(v < r):r = v
    print(r)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if(a[i] > k):
            r = int(a[i] / k)
            if((a[i] % k) > 0 ):r += 1
            count += r
        else:
            count += 1
    print(count)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n):
        v = l[i+1] - l[i]
        if(v < 0):
            print(l[i])
            break

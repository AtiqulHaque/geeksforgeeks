for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = num = 0
    for i in range(n):
        val = str(a[i])
        count = 0
        for j in range(len(val)):
            if(val[j] == "0"):count += 1
        if(r < count):
            r = count
            num = int(val)
        elif((r != 0) and r == count):
            if(int(val) > num):num = int(val)
    if(num == 0):
        print("-1")
    else:
        print(num)

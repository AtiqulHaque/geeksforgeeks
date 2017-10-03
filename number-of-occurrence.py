for _ in range(int(input())):
    r, f = map(int, input().split())
    l = list(map(int, input().split()))
    count = 0
    for i in range(r):
        if (l[i] == f):
            count += 1
    if(count == 0):
        print ("-1")
    else:        
        print (count)

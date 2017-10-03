for _ in range(int(input())):
    n = int(input())
    s = int(input().replace(' ',''),2)
    if(s == 0):
        print ("-1")
    else:
        l = list(bin(s)[2:])
        print(n - len(l))

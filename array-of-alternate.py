for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = []
    neg = []
    result = []
    for i in a:
        if(i < 0):neg.append(i)
        else: pos.append(i)

    t = True
    for i in range(n):
        if(t):
            if(len(pos) > 0):
                result.append(pos.pop(0))
            elif(len(neg) > 0):
                result.append(neg.pop(0))
        else:
            if(len(neg) > 0):
                result.append(neg.pop(0))
            elif(len(pos) > 0):
                result.append(pos.pop(0))

        if(t): t = False
        else: t = True

    for i in result:
        print(i,end=" ")
    print("")

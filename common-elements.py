def findValInList(val,l):
    for i in range(len(l)):
        if(l[i] > val):
            return False
        elif(l[i] == val):
            return True
    return False

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    h = []
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))
    n3 = list(map(int, input().split()))

    minLength = 0

    if(a < b and a < c):
        for i in n1:
            if(findValInList(i,n2) and findValInList(i,n3)):
                h.append(i)

    elif(c < b and c < a):
        for i in n3:
            if(findValInList(i,n1) and findValInList(i,n2)):
                h.append(i)
    else:
        for i in n2:
            if(findValInList(i,n1) and findValInList(i,n3)):
                h.append(i)

    if(len(h) == 0):
        print("-1")
    else:
        for i in h:
            print(i,end=" ")
        print("")

t = int(input())
ins = [0] * t
n = 0
f = 0
for i in range(t):
    n= int(input())
    ins[i] = list(map(int, input().split()))
    f = int(input())
    d = -1
    for j in range(len(ins[i])):
        if(ins[i][j] == f):
            if(d == -1):
                d = j
                print(d,end=" ")
            else:
                d = j

        if((len(ins[i]) -1) == j):
            print(d,end="")

    print("")

array = [0] * 100
n = [0] * 100
flag = 0
t = int(input())
for i in range(t):
    result = []
    n[i] = int(input())
    array[i] = [0] * n[i]
    array[i] = list(map(int, input().split()))

    flag = array[i][len(array[i]) - 1]
    result.append(flag)

    for j in range(2,len(array[i]) + 1):
        if(array[i][-j] >  flag):
            flag = array[i][-j]
            result.append(flag)
    for k in reversed(result):
        print(k,end=' ')

    print("")

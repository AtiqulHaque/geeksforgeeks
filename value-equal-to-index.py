t = int(input())

inputs = [0] * t
numInput = [0] * t

for i in range(t):
    numInput[i] = int(input())
    inputs[i] = list(map(int, input().split()))
    result = []
    for j in range(len(inputs[i])):
        c = j + 1
        if(c == inputs[i][j]):
            result.append(inputs[i][j])

    if(len(result) == 0):
        print ("Not Found")
    else:
        for k in result:
            print (k,end=" ")
        print("")

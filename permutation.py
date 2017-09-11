def permutation(data,index,fullResult,globalIndex):

    if(len(data) == 1):
        return fullResult.append(data[0])
    elif(len(data) == 2):
        if(index == ''):
            fullResult.append(data[0] + data[1])
            fullResult.append(data[1] + data[0])
            return fullResult
        else:
            return [index + data[0] + data[1] ] + [index + data[1] + data[0] ]
    else:
        pop = []
        NewPop = []
        globalIndex[len(data)-1] = index

        for i in range(len(data)):

            if(i > 0):
                temp = data[0]
                data[0] = data[i]
                data[i] = temp

            newIndex = data[0]
            newData = list(data[1 : len(data)])

            pop = permutation(newData,newIndex,fullResult,globalIndex)
            NewPop += pop

            pop = []

        if(index):
            for k in range(len(NewPop)):
                fullResult.append(globalIndex[len(data)] + index + NewPop[k])
        else:
            for k in range(len(NewPop)):
                fullResult.append(NewPop[k])
        return pop



t = int(input())
inputData = [0] * t

for i in range(t):
    inputData[i] = input()
    fullResult = []
    inputData[i] = list(inputData[i])
    inputData[i].sort()
    globalIndex = [0] * len(inputData[i])

    permutation(inputData[i],'',fullResult,globalIndex)
    for j in fullResult:
        print(j,end=' ')
    print("")

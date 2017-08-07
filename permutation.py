def permutation(data,index,fullResult):
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
        for i in range(len(data)):
            if(i > 0):
                temp = data[0]
                data[0] = data[i]
                data[i] = temp
            newIndex = data[0]
            newData = list(data[1 : len(data)])

            pop = permutation(newData,newIndex,fullResult)
            for j in range(len(pop)):
                fullResult.append(index + pop[j])
            pop = []
        return pop




inputData = "ABCD"
fullResult = []
permutation(list(inputData),'',fullResult)
print(fullResult)
print(len(fullResult))

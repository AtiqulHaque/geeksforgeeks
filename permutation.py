def permutation(index,data,result,fullResult):
    # A BGS -> # B GS
    # print (index,data)
    if(len(data) == 2):
        result.append(data[1] + data[0])
        result.append(data[0] + data[1])
        return result
    else:
        res = []
        ans = []
        for i in range(len(data)):
            newData = list(data)
            newIndex = newData[i]
            newData.remove(newIndex)
            res = permutation(newIndex,newData,result,fullResult)

            ans.append(res);
        print(ans)
        return fullResult


inputData = "ABSG"
result = []
response = []
fullResult = []
for i in range(len(inputData)):
    data = list(inputData)
    data.remove(data[i])
    permutation(inputData[i],data,result,fullResult)

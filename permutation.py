def permutation(index,data,result,fullResult):
    # A BGS
    if(len(data) == 2):
        result.append(index + data[1] + data[0])
        result.append(index + data[0] + data[1])
        fullResult.append(index + data[1] + data[0])
        fullResult.append(index + data[0] + data[1])
        return result
    else:
        res = []
        for i in range(len(data)):
            newData = data
            newIndex = data[i]
            newData.remove(newIndex)
            # B GS
            response = permutation(newIndex,newData,result,fullResult)
            print("Step return ",fullResult)
            return res





input = "ABSG"
result = []
fullResult = []
for i in range(len(input)):
    data = list(input)
    data.remove(data[i])
    permutation(input[i],data,result,fullResult)
    # print("first round returen when index",input[i])
    # print (result)
    # print(input[i],result)
    # for j in range(len(result)):
    #     print(input[i] + result[j])

# def factorial(n):
#     print("factorial has been called with n = " + str(n))
#     if n == 1:
#         return 1
#     else:
#         res = n * factorial(n-1)
#         print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
#         return res
#
#
# print(factorial(5))

# def mult3(n):
#     if n == 1:
#         return 3
#     else:
#         return mult3(n-1) + 3
#
# for i in range(1,10):
#     print(mult3(i))


# [0,1,2,3,4]

# def sum_n(n):
#     if(n == 0):
#         return 0
#     else:
#         return sum_n(n-1) + n
#
# print(sum_n(5s));

# Input number of test cases

# Problem :
# --------
# Given a array of n strings, find the longest common prefix among all strings present in the array.
#
# Input:
# The first line of the input contains an integer T which denotes the number of test cases to follow.
# Each test case contains an integer n. Next line has space separated n strings.
#
# Output:
# Print the longest common prefix as a string in the given array. If no such prefix exists print "-1"(without quotes).
#
# Constraints:
# 1<=T<=100
# 1<=n<=100
# 1<=|S|<=100
#
# Example:
# Input:
# 2
# 4
# geeksforgeeks geeks geek geezer
# 3
# apple ape april
#
# Output:
# gee
# ap


t = int(input())
stData = [0] * t
nith = [0] * t
def sequence(strList,index,result):

    indexValue = ''
    count = 0
    totalString = len(strList)

    if(totalString == 1):
        return strList[0]

    for i in range(totalString):
        count += 1
        if(index > len(strList[i])-1):
            return result

        if(indexValue == ''):
            indexValue = strList[i][index]
        elif(strList[i][index] == indexValue):
            if(count == totalString):
                result.append(indexValue)
                return sequence(strList,index + 1,result)
        else:
            return result

# result = [0]

for i in range(t):
    nith[i] = int(input())
    stData[i] = list(map(str, input().split()))
    outPut = sequence(stData[i],0,[])
    st = ''
    if(outPut is None or len(outPut) == 0):
        print ("-1")
    else:
        for i in range(len(outPut)):
            st += outPut[i]
        print (st)

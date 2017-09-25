import math
def setFrequency(strs):
    result = {}
    if(strs == ''):
        return result
    else:
         strs = list(strs)
         for i in range(len(strs)):
             result[strs[i]] = result.get(strs[i],0) + 1
    return result

def minimizeSum(frequency,k):
    maxFrequency = 0
    maxFrequencyCh = ''
    end = False
    for j, v in frequency.items():
        if(maxFrequency < v):
            maxFrequency = v
            maxFrequencyCh = j

    if(maxFrequency == 0):
        return frequency
    maxFrequency = maxFrequency -1
    k = k - 1

    if(k < 0):
        end = True
        k = k * -1
        frequency[maxFrequencyCh] = k
    elif(k == 0):
        end = True
        frequency[maxFrequencyCh] = maxFrequency
    else:
        frequency[maxFrequencyCh] = maxFrequency

    if(end):
        return frequency;
    else:
        return minimizeSum(frequency,k)

t = int(input())

inputString = [0] * t
numInput = [0] * t
k = [0] * t

for i in range(t):
    inputString[i] = input()
    k[i] = int(input())
    frequency = setFrequency(inputString[i])
    frequency = minimizeSum(frequency,k[i])
    sum = 0
    for val in frequency.values():
        if val > 1:
            sum += math.pow(val ,2)
        else:
            sum += val

    print (math.floor(sum))

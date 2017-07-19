# Problem :
# ------------
# Twice counter
#
# Description
# -----------
# Given an array of n words. Some words are repeated twice, we need count such words.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. Each test case contains an integer n denoting the number of words in the string.
# The next line contains n space separated words forming the string.
#
# Output:
# Print the count of the words which are repeated twice in the string.
#
# Constraints:
# 1<=T<=10^5
# 1<=no of words<=10^5
# 1<=length of each word<=10^5
#
# Example:
# Input:
# 2
# 10
# hate love peace love peace hate love peace love peace
# 8
# Tom Jerry Thomas Tom Jerry Courage Tom Courage
#
# Output:
# 1
# 2

t = int(input())
numOfWord = [0] * t
words  = [0] * t

def compareWord(word1,word2):
    if((len(word1) != len(word2)) or (word1[0] != word2[0])):
        return False
    for i in range(len(word1)):
        if(word1[i] != word2[i]):
            return False
    return True



def removeItems(the_list, val):
    return [value for value in the_list if value != val]



def countTwice(words,index,result):
    if((len(words) == 0) or(index == len(words) - 1)):
        return result

    for i in range(len(words)):
        if(compareWord(words[index],words[i])):
            if(words[index] in result):
                result[words[index]] = int(result[words[index]]) + 1
            else:
                result[words[index]] = int(1)

    return countTwice(removeItems(words,words[index]),index,result)

for i in range(t):
    numOfWord[i] = int(input())
    words[i] = list(map(str, input().split()))
    index = 0
    count = 0
    for j in countTwice(words[i],index,{}).values():
        if(j == 2):
            count += 1
    print (count)

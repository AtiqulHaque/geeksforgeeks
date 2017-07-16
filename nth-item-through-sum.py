"""
Given two sorted arrays, we can get a set of sums(add one element from the first and one from second). Find the N’th element in the set considered in sorted order.
Note: Set of sums should have unique elements.
--------------------------------------------------

Input : arr1[] = {1, 2}
        arr2[] = {3, 4}
        N = 3
Output : 6
We get following elements set of sums.
4(1+3), 5(2+3 or 1+4), 6(2+4)
Third element in above set is 6.

Input : arr1[] = {1, 3, 4, 8, 10}
        arr2[] = {20, 22, 30, 40}
        N = 4
Output : 25
We get following elements set of sums.
21(1+20), 23(1+22 or 20+3), 24(20+4), 25(22+3)...
Fourth element is 25.



-------------------------------------

Input:
The first line of input contains an integer T denoting tghe number of test cases. Then T test cases follow. Each test case contains two integers m and n denoting the size of the two arrays respectively. The next two lines contains m and n space separated elements forming both the arrays respectively. The last line contains the value of N.

Output:
Print the value of Nth element in set. If Nth element doesn't exist in set print -1.

Constraints:
1<=T<=10^5
1<=m,n<=10^5
1<=arr1[i],arr2[j]<=10^5
1<=N<=m*n

Example:
Input:
2
2 2
1 2
3 4
3
5 4
1 3 4 8 10
20 22 30 40
4

Output:
6
25

"""



import math
# Input number of test cases
t = int(input())
arr = [0] * t
l1 = [0]* t
l2 = [0]* t
nth = [0]* t

def binarySearchInsertion(item, itemList):

    if len(itemList) == 0:
        itemList.append(item)
        return itemList

    if len(itemList) == 1:
        if itemList[0] == item:
            return itemList

        itemList.append([])

        if itemList[0] > item :
            temp = itemList[0]
            itemList[0] = item
            itemList[1] = temp
        else:
            itemList[1] = item
        return itemList


    start = 0
    end = len(itemList) - 1


    while True:
        calculate = end - start
        if(calculate == 1):
            if itemList[end] == item or itemList[start] == item:
                return itemList
            if item > itemList[end]:
                itemList.append([])
                for i in range(end + 1,len(itemList)):
                    temp = itemList[i]
                    itemList[i] = item
                    item = temp
                return itemList
            else:
                itemList.append([])
                for i in range(start,len(itemList)):
                    temp = itemList[i]
                    itemList[i] = item
                    item = temp
                return itemList

        mid = math.ceil((start + end) / 2)

        if itemList[mid] > item:
            end = mid
        if itemList[mid] < item:
            start = mid
        if itemList[mid] == item:
            return itemList

# print(binarySearchInsertion(4,[4,5]))

for i in range(t):
    arr[i] = list(map(int, input().split()))
    l1[i] = list(map(int, input().split()))
    l2[i] = list(map(int, input().split()))
    nth[i] = int(input())
    r = []
    for j in range(len(l1[i])):
        for k in range(len(l2[i])):
            temp = l1[i][j] + l2[i][k]
            binarySearchInsertion(temp,r)

    print (r[nth[i] - 1])


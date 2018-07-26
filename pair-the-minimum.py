def bubbleSort(data):
    """Bubble sort Function."""
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if(int(data[i]) > int(data[j])):
                temp = int(data[j])
                data[j] = int(data[i])
                data[i] = temp
    return data


for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))

    if(n == 1):
        print("(" + str(l1[0]) + "," + str(l1[1]) +  ")")
    else:
        sortedList = bubbleSort(l1)
        listLen = int(len(sortedList) / 2)
        l = len(sortedList) - 1
        for i in range(listLen):
            print("(" + str(sortedList[i]) + "," + str(sortedList[l - i]) +  ")",end = '')
        print('')

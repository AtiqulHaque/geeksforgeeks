
def anagram(s):
    s = list(s)
    middle = len(s)%2
    if middle != 0:
        return -1
    firstPart = s[0:int(len(s)/2)]
    lastPart = s[int(len(s)/2):]
     

    first = {}
    last = {}
    for i in firstPart:
        if i in first.keys():
            first[i] = first[i] + 1 
        else:
            first[i] = 1 


    for i in lastPart:
        if i in last.keys():
            last[i] = last[i] + 1 
        else:
            last[i] = 1 
    total = 0
    print(first,last)

    for k in last.keys():
        if k in first.keys():
            rest = first[k] - last[k]
            if rest < 0:
                rest = rest * -1
             
            first[k] = rest
            last[k] = rest
    
    for k in last.keys():
        if last[k] != 0:
            total += last[k]


    print(first,last)
    return total

print(anagram("fdhlvosfpafhalll"))



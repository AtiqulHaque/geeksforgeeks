digitSet = {
1:True,
2:True,
3:True,
4:True,
5:True
}
for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n+1):
        val = str(i)
        if(len(val) == 1):
            if(int(val) in digitSet.keys()):
                count += 1
        else:
            found = True
            for j in range(len(val)):
                if(int(val[j]) not in digitSet.keys()):
                    found = False
                    break
            if(found): count += 1
    print(count)

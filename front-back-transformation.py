smChStart = 97
smChEnd = 122
cpChStart = 65
cpChEnd = 90
for _ in range(int(input())):
    st = str(input())
    revSt = ''
    for i in st:
        if(ord(i) >= smChStart and ord(i) <= smChEnd):
            dif = (smChEnd - ord(i)) + smChStart
            revSt += chr(dif)
        elif(ord(i) >= cpChStart and ord(i) <= cpChEnd):
            dif = (cpChEnd - ord(i)) + cpChStart
            revSt += chr(dif)
    print(revSt)

cpChStart = 65
cpChEnd = 90
for _ in range(int(input())):
    st = str(input())
    count = 1
    for i in st:
        if(ord(i) >= cpChStart and ord(i) <= cpChEnd):
            count += 1
    print(count)

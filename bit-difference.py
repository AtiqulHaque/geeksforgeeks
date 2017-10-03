
def dec_to_bin(x):
    return bin(x)[2:]

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = a ^ b
    c = dec_to_bin(c)
    count = 0
    for i in list(c):
        if(int(i) == 1):
            count += 1
    print (count)


def dec_to_bin(x):
    return bin(x)[2:]


t = int(input())
for i in range(t):
    n = int(input())
    if(n == 0):
        print (0)
    else:
        h = list(dec_to_bin(n))
        h.reverse()
        for j in range(len(h)):
            if(h[j] == '1'):
                print(j + 1)
                break

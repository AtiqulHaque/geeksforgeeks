import math
factor = [2,3,5]
prims = {}
def isPrime(m):
    p = True
    if(m == 2):
        prims[m] = True
        return prims[m]

    if m in prims.keys():
        return prims[m]
    for i in range(2,math.ceil(math.sqrt(m)) + 1):
        v = m / i
        if(v.is_integer()):
            p = False
    prims[m] = p

    return prims[m]

def getPrimeFactor(n,f):
    for i in range(2,math.ceil(math.sqrt(n)) + 1):
        v = n / i
        if(v.is_integer()):
            f.append(i)
            if(isPrime(int(v)) == True):
                f.append(int(v))
                return f
            else:
                return getPrimeFactor(v,f)
    return f

for _ in range(int(input())):
    n = int(input())
    d = 10000000
    primeN = [1]
    for i in range(2,d):
        if(isPrime(i) == True):
            if(i in factor):
                primeN.append(i)
        else:
            f = []
            found = True
            getPrimeFactor(i,f)

            for j in f:
                if(j not in factor):
                    found = False
            if(found):
                primeN.append(i)
        if(len(primeN) == n):
            print(primeN[n - 1])
            break

# t= int(input())
# for _ in range(t):
#     n=int(input())
#     ugly=[0]*n
#     ugly[0]=1
#     i2=i3=i5=0
#     n2=2
#     n3=3
#     n5=5
#     for i in range(1,n):
#         ugly[i] = min(n2,n3,n5)
#         if(ugly[i]==n2):
#             i2+=1
#             n2=ugly[i2]*2
#         if(ugly[i]==n3):
#             i3+=1
#             n3=ugly[i3]*3
#         if(ugly[i]==n5):
#             i5+=1
#             n5=ugly[i5]*5
#     print(ugly[-1])

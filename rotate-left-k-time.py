# for _ in range(int(input())):
#     i = list(map(int, input().split()))
#     t = [0]*i[0]
#     m = list(map(int, input().split()))
#     for j in range(i[0]):
#         t[j] = m[i[1]*j:i[1]*(j + 1)]
#
#     for k in range(len(t)):
#         for l in range(i[2]):
#             for n in range(len(t[k]) - 1):
#                 temp = t[k][n]
#                 t[k][n] = t[k][n + 1]
#                 t[k][n + 1] = temp
#     for k in range(len(t)):
#         for n in range(len(t[k])):
#            print(t[k][n],end=" ")
#     print("")
#code
num=int(input())
while num>0:
    num-=1
    m,n,k=map(int,input().split())
    matrix=input().split();
    for i in range(0,m):
        start=(i)*n;
        j=0;
        while j<n:
            index=(j+k)%n
            print(matrix[start+index], end=' ')
            j+=1;
    print('')



    

import math
for _ in range(int(input())):
    letters = input()
    l = math.sqrt(len(letters))
    if(l.is_integer()):
        n = int(l)
        m = int(l)
        mat = [[0 for x in range(n)] for x in range(m)]
        for i in range(n):
            for j in range(m):
                print(i,j)
                mat[i][j] = letters[(i * n) + j]

        for i in range(n):
            for j in range(m):
                print(mat[j][i])


        print(mat)

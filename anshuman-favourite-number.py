for _ in range(int(input())):
    n = int(input())
    if(n < 0): n = -1 * n
    if(n % 5 == 0):
        print("YES")
    else:
        print("NO")

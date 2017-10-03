for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l1.sort()
    l2.sort()

    equal = 1

    for i in range(len(l1)):
        if(l1[i] != l2[i]):
            equal = 0
            break;

    print(equal)

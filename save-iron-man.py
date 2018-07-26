for _ in range(int(input())):
    ustr = input()
    ustr = ''.join(e for e in ustr if e.isalnum()).lower()
    isPalindrom = True
    for i in range(int(len(ustr) / 2)):
        if(ustr[i] != ustr[(len(ustr) - 1) - i]):
            isPalindrom = False

    if(isPalindrom):
        print("YES")
    else:
        print("NO")

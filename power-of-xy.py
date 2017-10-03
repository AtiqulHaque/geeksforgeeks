import math

def getReminder(fac,num,p):
    reminder = num / fac
    p += 1
    if(reminder == (1.0)):
        if(p == 1):
            return False
        else:
            return True
    if(reminder.is_integer()):
        return getReminder(fac,int(reminder),p)
    else:
        return False



for _ in range(int(input())):
    a = int(input())
    if(a == 1):
        print(1)
    else:
        n = math.sqrt(a)
        if(n.is_integer() == False):
            n = math.ceil(n)
        f = False
        for i in range(2,int(n) + 1):
            if(getReminder(i,a,0)):
                f = True
                break
        if(f):
            print(1)
        else:
            print(0)

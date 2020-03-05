import time # line number 1
import random

from auto_profiler import Profiler, Tree

def f1():
    mysleep(.6+random.random())

def mysleep(t):
    time.sleep(t)

def fact(i):
    f1()
    if(i==1):
        return 1
    return i*fact(i-1)


def show(p):
    print('Time   [Hits * PerHit] Function name [Called from] [Function Location]\n'+\
          '-----------------------------------------------------------------------')
    print(Tree(p.root, threshold=0.5))

@Profiler(depth=4, on_disable=show)
def main():
    for i in range(5):
        f1()

    fact(3)


if __name__ == '__main__':
    main()
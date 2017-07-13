# -*- coding: utf-8 -*-
"""Bubble sort algorithiem implementation."""

""""LALU wanted to purchase a laptop so he went to a nearby sale.
There were n Laptops at a sale.
Laptop with index i costs ai rupees. Some Laptops have a negative price
— their owners are ready to pay LALU if he buys their useless Laptop. LALU
can buy any Laptop he wants. Though he's very strong, he can carry at most m
Laptops, and he has no desire to go to the sale for the second time. Please
help LALU find out the maximum sum of money that he can earn."""


def bubbleSort(data):
    """Bubble sort Function."""
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if(int(data[i]) > int(data[j])):
                temp = int(data[j])
                data[j] = int(data[i])
                data[i] = temp
    return data

data = []
testCase = int(raw_input())
while(testCase):
    scope = raw_input()
    scope = scope.split(' ')
    inputList = raw_input()
    data = inputList.split(' ')
    data = bubbleSort(data)
    sumVal = 0
    for i in data[0:int(scope[1])]:
        sumVal += int(i)
    if(sumVal < 0):
        print sumVal * -1
    else:
        print 0
    testCase = testCase - 1

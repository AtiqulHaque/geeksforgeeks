#code

def getLongGestPrefix(left,right):
    result = ''
    if left == None:
        return right
    if right == None:
        return left
    i = 0
    n = len(left) - 1
    m = len(right) - 1

    while True:
        if i > n or i > m:
            break

        if left[i] == right[i]:
            result += left[i]
            i = i + 1
        elif left[i] != right[i]:
            break
    return result





# t = int(input())

# for i in range(t):
#     n = int(input())
#     result= None
#     iData = list(map(str, input().split()))
#     for i in iData:
#         result = getLongGestPrefix(result, i)
#     if result == '':
#         print("-1")
#     else:
#         print(result)

def longestPrefixSuffix(s) : 
    n = len(s) 
      
    for res in range(n // 2, 0, -1) : 
          
        # Check for shorter lengths 
        # of first half. 
        prefix = s[0: res] 
        suffix = s[n - res: n] 
    
        if (prefix == suffix) : 
            return res 
              
  
    # if no prefix and suffix match  
    # occurs 
    return 0
      
s = "blablabla"
print(longestPrefixSuffix(s)) 
  
# This code is contributed by Nikita Tiwari. 
    
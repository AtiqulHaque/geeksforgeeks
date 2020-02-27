def matchParenthisis(mt):
    exp = {
        "{" : "}",
        "[" : "]",
        "(" : ")",
    }
    stack = []
    
    for i in mt:
        if i in exp.keys():
            stack.append(i)
        else:
            if not stack:
                return "Not balanced"
            r = stack.pop()
            if exp[r] != i:
                return "Not balanced"
                
    if len(stack) != 0:
        return "Not balanced"
    else:
        return "balanced"
   
t = int(input())

for i in range(t):
    intp = input()
    print(matchParenthisis(intp))


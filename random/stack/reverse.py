def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(el,stack):
    stack.append(el)
    return stack

def pull(stack):
    

def reverse(string):
    st = list(string)
    s = ''
    while True:
        if not st:
            break
        else:
            s += st.pop()
    return s   
        


print(reverse("asdfghjkl"))
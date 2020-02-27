
def superReducedString(s):
    inp = "The quick brown fox jumps over the lazy dog"
    de = {}
    for i in inp:
        if i != ' ':
            de[i.lower()] = 0
    for i in s:
        if i != ' ':
            de[i.lower()] = 1
    for i in de:
        if de[i] == 0:
            return "not pangram"
    return "pangram"
            


print(superReducedString("we promptly judged antique ivory buckles for the prizex"))

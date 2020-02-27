def hackerrankInString(s):
    d = "hackerrank"
    i = j = 0

    dL = len(d) - 1 
    sL = len(s) - 1

    while True:
        if i > dL:
            return "Yes"
        else:
            if j > sL :
                return "No"
            else:
                if d[i] == s[j]:
                    i += 1 
                    j += 1
                else:
                    j += 1


print(hackerrankInString("hereiamstackerrank"))

print("S".isupper())

def lsp(pattern):
	lspAr = [0] * len(pattern)
	i = 1
	j = 0
	n = len(pattern)  -1
	while(True):
		if i >= n:
			prev = j -1
			if pattern[i] == pattern[lspAr[prev]]:
				lspAr[i] = lspAr[prev] + 1
			break

		elif pattern[i] == pattern[j]:
			lspAr[i] = j + 1
			i += 1
			j += 1

		elif pattern[i] != pattern[j]:
			lspAr[i] = 0
			i += 1
	return lspAr
				


def searchPattrn(patt,text,lspAr):
    m = len(patt) - 1
    n = len(text) - 1
    j = 0
    i = 0
    
    while True:
        if i > n:
            break
        elif j == m:
            print("match",i)
            i += 1
            j = 0 
        elif patt[j] == text[i]:
            i += 1
            j += 1
        elif patt[j] != text[i]:
            prev = j - 1
            j = lspAr[prev]
            if patt[j] == text[i]:
                i += 1
                j += 1
            else:
                i += 1
    return True
            

s= "AACDAACD" 
pat = "ACDA"
lspAr = lsp("ACDA")

searchPattrn(pat,s,lspAr)


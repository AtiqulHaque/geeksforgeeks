def searchPattrn(patt,text):
	m = len(patt) - 1
	n = len(text) - 1
	
	for i in range(n-m + 1):
		j = 0
		while True:
			if j > m:
				break
			else:
				if patt[j] != text[i+j]:
					break
				if j == m:
					print("Pattarn found in ",i)
					break
				else:
					j += 1
	

s= "AABAACAADAABAAABAA" 
pat = "AABA"

searchPattrn(pat,s)

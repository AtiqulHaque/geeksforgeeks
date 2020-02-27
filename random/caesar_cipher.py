def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
        if i.isalpha():
            # Encrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + s-65) % 26 + 65) 
    
            # Encrypt lowercase characters 
            else: 
                result += chr((ord(char) + s - 97) % 26 + 97) 
        else:
            result += char
  
    return result 
  
#check the above function 


def caesarCipher(s, k):
    outPut = []
    upperMax = 90
    upperMin = 65
    lowerMax = 122
    lowerMin = 97
    for i in s:
        if i.isalpha():
            if i.isupper():
                chNumb = ord(i) + k
                if chNumb > upperMax:
                    chNumb = chNumb - upperMax
                    chNumb = upperMin + chNumb - 1
                    outPut.append(chr(chNumb))
                else:
                    outPut.append(chr(chNumb))

            if i.islower():
                chNumb = ord(i) + k
                if chNumb > lowerMax:
                    chNumb = chNumb - lowerMax - 1
                    chNumb = lowerMin + chNumb
                    outPut.append(chr(chNumb))
                else:
                    outPut.append(chr(chNumb))
        else:
            outPut.append(i)

    print(outPut)
    return ''.join(outPut)


#print("letter's;")
#print(caesarCipher("letter'[]{}78s;",2))
#print(chr((ord("z") + 3-65) % 26 + 65) )

# text = "www.abc.xy"
# s = 87
# print ("Text  : " + text )
# print ("Shift : " + str(s)) 
# print ("Cipher: " + encrypt(text,s)) 

# text = "www.abc.xy"
# s = 87
# print ("Text  : " + text )
# print ("Shift : " + str(s)) 
# print ("Cipher: " + caesarCipher(text,s)) 

print(16%5)
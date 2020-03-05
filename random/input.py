# #code
# for _ range(int(input())):
#     n = int(input())
#     stt = list(map(str, input()))
#     i = 0
#     j = len(stt) - 1
    
#     while True:
#         if i == j:
#             break
#         if stt[i].isalpha() == False:
#             i += 1
#             continue
#         if stt[j].isalpha() == False:
#             j -= 1
#             continue
    
#         temp = stt[i]
#         stt[i] = stt[j]
#         stt[j] = temp
#         i += 1
#         j -= 1
    
         
#     print(stt)


myDic = {"a" : 2,"b" : 2,"c" : 1}
print(myDic.pop("c"), myDic)
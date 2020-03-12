from collections import deque 


for _ in range(int(input())):
    graph = {}
    
    iData = list(map(int,input().split(' ')))

    for i in range(0, len(iData), 2):
        j = i + 1
        
        if j > len(iData) - 1:
            break

        if graph.get(iData[i]) != None:
            graph[iData[i]].append(iData[j])
        else:
            graph[iData[i]]= [iData[j]]

    print(iData, graph)

    visited = []
    q = deque() 
    allNodes = list(graph.keys())

    # visited.append(allNodes[0])
    q.append(allNodes[0])

    while q:
        i = q.pop()
        if i not in visited:
            visited.append(i)
            if i in allNodes:
                for j in graph[i]:
                    q.append(j)



















        # for e in graph[i]:
        # if i not in visited:
        #     visited.append(i)
        #     if  i in graph.keys():
        #         for j in graph[i]:
        #             q.append(j)

    # for i in graph.keys():
    #     if i not in visited:
    #         visited.append(i)
    #         for j in graph[i]:
    #             q.append(j)
        
    #     while len(q) != 0:
    #         k = q.popleft()
    #         visited.append(k)
    #         if k in graph.keys():
    #             for l in graph[k]:
    #                 q.append(l)
                    

print(visited)
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
    myStack = []


    for i in range(graph.keys()):
        if i not in visited:
            
            visited.append(i)
            for j in graph[i]:
                myStack.append(j)


                


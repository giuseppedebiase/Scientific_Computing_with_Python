my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    #Unvisited nodes
    unvisited = list(graph)
    #Distances from starting node to X node
    distances = {node: 0 if node == start else float('inf') for node in graph}
    #Paths from starting node to X node
    paths = {node: [] for node in graph}
    paths[start].append(start)

    #The while continues until all the nodes have been visited
    while unvisited:
        #Choses the current node based on the minimum distance from the starting node
        current = min(unvisited, key=distances.get)
        #Checks neighboring nodes of the current node
        for node, distance in graph[current]:
            #If the distance between current node-neighboring node + distance current node-starting node is
            #less than the current known distance starting node-neighboring node
            #the minimum distance between starting node and neighboring node get updated
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                #Subsitutes the shortest path to node with a new, shorter, path (if found)
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    #The shortest path that leads to the neighboring node of current passes by current
                    #E.g. if current = D, neighbour node = C and path to D is [A, D] -> 
                    #the path that leads to the C will include [A, D] (C will be added to path[C] with line 39)
                    paths[node].extend(paths[current])
                #Adds the neighbouring node of current to the path that leads to node (which is neighbouring node)
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')

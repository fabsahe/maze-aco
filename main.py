# algoritmo de hormigas para solucion de laberintos

from node import Node
from ant import Ant
from p1functions import *

node_list = []

if __name__ == '__main__':
    rows, cols = map(int, input().split())
    maze_list = [input() for _ in range(rows)]


    for i in range(rows):
        r = maze_list[rows-(i+1)]
        for j in range(len(r)):
            if r[j] == ' ':
                b = [j+1,i+1]
                node_list.append(b)

    nodes = {}
    for nodeCoor in node_list:
        nodes[tuple(nodeCoor)] = Node(tuple(nodeCoor))
    for nodeCoor in nodes:
        for x in range(7):
            for y in range(7):
                if (x, y) != nodeCoor and keyExist(nodes, (x,y)):
                    if (x==nodeCoor[0] and abs(y-nodeCoor[1]) == 1) or (y==nodeCoor[1] and abs(x-nodeCoor[0]) == 1):
                        nodes[nodeCoor].add_connected_node(nodes[(x, y)])
    
    # Colocar aqui la informacion del laberinto
    entrance = nodes[(3, 1)]
    exits = [nodes[(5, 6)]]
    mazeSize = [cols, rows]
    
    n_ant = 50
    alpha = 1
    rho = 0.1
    initial_pheromone = 0.1
    for nodeCoor in nodes:
        nodes[nodeCoor].set_pheromone(initial_pheromone)
    ants = [Ant() for _ in range(n_ant)]
        
    max_iteration = 200
    percentage_of_dominant_path = 0.9
    iteration = 0
    
    
    while iteration < 200 and get_percentage_of_dominant_path(ants) < percentage_of_dominant_path:
        for ant in ants:
            ant.reset()
            ant.get_path(entrance, exits, alpha)
        
        for node in nodes:
            nodes[node].evaporate_pheromone(rho)
            nodes[node].deposit_pheromone(ants)
            
        iteration += 1
        
    paths = []
    pathsCount = []
    for ant in ants:
        if ant.nodes not in paths:
            paths.append(ant.nodes)
            pathsCount.append(1)
        else:
            pathsCount[paths.index(ant.nodes)] += 1
    pathIndex = pathsCount.index(max(pathsCount))
    solution = paths[pathIndex]
    print("Solucion = [", end = "")
    for i in range(len(solution)-1):
        print(solution[i].coordinates, end = ", ")
    print(str(solution[-1].coordinates) + "]")
    print("Longitud del camino: " + str(len(solution)))
    print("Iteraciones: " + str(iteration))

    
            
        
        
        



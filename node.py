class Node:
    def __init__(self, coordinates, pheromone = 0):
        self.coordinates = coordinates #(x, y)
        self.pheromone = pheromone
        self.connected_nodes = []
        
    def add_connected_node(self, node):
        if node not in self.connected_nodes:
            self.connected_nodes.append(node)
        
    def set_pheromone(self, pheromone):
        self.pheromone = pheromone
        
    def evaporate_pheromone(self, rho):
        self.pheromone = (1-rho) * self.pheromone
        
    def deposit_pheromone(self, ants):
        totalDeposition = 0
        for ant in ants:
            if self in ant.nodes:
                totalDeposition += (1/ant.get_path_length())
        self.pheromone += totalDeposition    



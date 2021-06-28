import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def keyExist(dicti, key): 
    if key in dicti.keys(): 
        return True
    else: 
        return False
    
def get_percentage_of_dominant_path(ants):
    paths = []
    pathsCount = []
    for ant in ants:
        if len(ant.nodes) == 0:
            return 0
        if ant.nodes not in paths:
            paths.append(ant.nodes)
            pathsCount.append(1)
        else:
            pathsCount[paths.index(ant.nodes)] += 1
    percentage = max(pathsCount)/sum(pathsCount)
    return percentage  

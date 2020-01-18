#from variables import *
#from functions import *
#from main import *
      
class Graph():

    def __init__(self, graph, dimensions, x=0, y=0):
        self.x = x
        self.y = y
        self.graph = graph
        self.dimensions = dimensions
        self.size = dimensions*dimensions
        self.instructions = [0] * self.size

    def adjacentTo(self, posOne, posTwo):
        if posOne[0] == posTwo[0]:
            if posOne[1]+1 == posTwo[1]:
                return True
            if posOne[1]-1 == posTwo[1]:
                return True
            
        if posOne[1] == posTwo[1]:
            if posOne[0]+1 == posTwo[0]:
                return True
            if posOne[0]-1 == posTwo[0]:
                return True

        return False
    
    def isValid(self, pos, v, path):
        
        for vertex in path:
            if vertex == pos:
                return False

        if pos[0] < 0 or pos[0] >= self.dimensions:
            return False
        
        if pos[1] < 0 or pos[1] >= self.dimensions:
            return False
        
        return True

    def move(self, pos, direction):
        currentPos = pos.copy()
        if direction == 1:
            currentPos[0] += 1
        elif direction == 2:
            currentPos[0] -= 1
        elif direction == 3:
            currentPos[1] += 1
        elif direction == 4:
            currentPos[1] -= 1

        return currentPos
    
    def hamCycleUtil(self, v, path):

        pos = path[v]
        
        if v == self.size - 1:
            
            if self.adjacentTo(self.graph[0], path[v]):
                return True
            else:
                return False

        for d in range(1, 5):
            test = self.move(pos,d)
            
            if self.isValid(test, v, path):
                
                path[v+1] = test
                self.instructions[v] = d

                if self.hamCycleUtil(v+1, path) == True:
                    return True

                path[v+1] = [-1,-1]
                self.instructions[v] = 0

        return False

    def hamCycle(self):
        path = [[-1,-1]] * self.size
        path[0] = [self.x,self.y]

        if self.hamCycleUtil(0, path) == False:
            print("NO SOLUTION\n")
            return False

        self.finalMove(path)
        self.printSolution(path)
        return True

    def finalMove(self, path):
        pos = path[self.size-1]
        for d in range(1, 5):
            test = self.move(pos,d)
            if test == path[0]:
                self.instructions[self.size-1] = d
    
    def printSolution(self, path):
        print("Solution Exists\n")
        #for vertex in path:
            #print (vertex)
        print(path)
        print(self.instructions)
        #print(str(path[0]) + "\n")

dim = 5
coordinates = []
for x in range(dim):
    for y in range(dim):
        coordinates.append([x,y])

print(coordinates)
graph = Graph(coordinates, dim, 0, 0)
graph.hamCycle();






            

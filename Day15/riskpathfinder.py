import copy
import sys
from collections import deque
class PathFinder:
    def __init__(self):
        self.risk_map_file = 'riskmap.txt'
        self.riskmap = []
        self.total_rows=0
        self.total_columns=0
        self.completepaths = []
        self.row = [-1, 0, 0, 1]
        self.col = [0, -1, 1, 0]

    def getRiskmap(self):
        with open(self.risk_map_file) as f:
            self.riskmap = [list(line.strip()) for line in f]
            self.total_rows = len(self.riskmap)
            self.total_columns = len(self.riskmap[0])
            for r in range(0, self.total_rows):
                for c in range(0,self.total_columns):
                    self.riskmap[r][c] = int(self.riskmap[r][c]) #turn 2D array into ints
                    
    def extendMap(self):
        for i in range(0,self.total_rows): #extend to the right
            line = self.riskmap[i]
            add_to_right = []
            for j in range(1,5):
                for x in line:
                    num_to_add = x+j
                    if num_to_add > 9:
                        num_to_add = num_to_add - 9
                    add_to_right.append(num_to_add)
            self.riskmap[i] = self.riskmap[i] + add_to_right
        copy_map = copy.deepcopy(self.riskmap)
        for c in range(1, 5):
            curr_copy = copy.deepcopy(copy_map)
            for a in range(0,len(curr_copy)):
                for b in range(0,len(curr_copy[a])):
                    num_to_add = curr_copy[a][b] + c
                    if num_to_add > 9:
                        num_to_add = num_to_add - 9
                    curr_copy[a][b] = num_to_add
            self.riskmap.extend(curr_copy)
        self.total_rows = len(self.riskmap)
        self.total_columns = len(self.riskmap[0])     
                
    def getFullPath(self):
        self.getRiskmap()
        self.extendMap()
        #path_weight = [[0 for i in range(0,self.total_rows)] for j in range(0,self.total_columns)]
        
        path = self.findPath(self.riskmap)
        
        return path


 
 
    # The function returns false if (x, y) is not a valid position
    def isValid(self, x, y, N):
        return (0 <= x < N) and (0 <= y < N)
 
 
 
    def findPath(self, matrix, x=0, y=0, level=0):
     
        # base case
        if not matrix or not len(matrix):
            return
     
        # `N × N` matrix
        N = len(matrix)
     
        # create a queue and enqueue the first node
        q = deque()
     
        # (x, y) represents coordinates of a cell in the matrix
        # `level` stores the distance of a current node from the source node
        # (i.e., BFS level)
     
        q.append((x, y, level))
     
        # set to check if the matrix cell is visited before or not
        visited = set()
        visited.add((x, y))
     
        # loop till queue is empty
        while q:
     
            # dequeue front node and process it
            i, j, level = q.popleft()
     
            # return if the destination is found
            if i == N - 1 and j == N - 1:
                return level
     
            # value of the current cell
            n = matrix[i][j]
     
            # check all four possible movements from the current cell
            # and recur for each valid movement
            for k in range(len(self.row)):
                # get next position coordinates using the value of the current cell
                x = i + self.row[k]
                y = j + self.col[k]
     
                # check if it is possible to go to the next position
                # from the current position
                if self.isValid(x, y, N):
                    # if it isn't visited yet
                    if (x, y) not in visited:
     
                        # construct the next cell node and enqueue it
                        # and mark it as visited
                        q.append((x, y, level + matrix[x][y]))
                        visited.add((x, y))
     
        # return a negative number if the path is not possible
        return -1
        
    def getShortestPath(self):
        self.getRiskmap()

        path_weight = [[0 for i in range(0,self.total_rows+1)] for j in range(0,self.total_columns+1)]

        for i in range(1, self.total_rows+1):
            for j in range(1, self.total_columns+1):
                if path_weight[i-1][j] == 0:
                    path_weight[i][j] = path_weight[i][j-1]+self.riskmap[i-1][j-1]
                elif path_weight[i][j-1] == 0:
                    path_weight[i][j] = path_weight[i-1][j] +self.riskmap[i-1][j-1]
                else:
                    path_weight[i][j] = (
                        min(path_weight[i-1][j],path_weight[i][j-1])
                        +self.riskmap[i-1][j-1]
                        )

        return (path_weight[self.total_rows][self.total_columns]-self.riskmap[0][0])

# A queue node used in BFS
class Node:
    # (x, y) represents coordinates of a cell in the matrix
    # maintain a parent node for the printing path
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
 
    def __repr__(self):
        return str((self.x, self.y))
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


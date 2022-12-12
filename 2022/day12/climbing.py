import sys
from collections import deque
class Climber:
    def __init__(self):
        self.input = 'input.txt'
        self.climbmap = []
        self.total_rows=0
        self.total_columns=0
        self.start = (0,0)
        self.end = (0,0)
        self.row = [-1, 0, 0, 1]
        self.col = [0, -1, 1, 0]

    def process(self):
        with open(self.input) as f:
            self.climbmap = [list(line.strip()) for line in f]
            self.total_rows = len(self.climbmap)
            self.total_columns = len(self.climbmap[0])
            for r in range(0, self.total_rows):
                for c in range(0,self.total_columns):
                    if self.climbmap[r][c] == 'S':
                        self.start = (r,c)
                        self.climbmap[r][c] = 97
                    elif self.climbmap[r][c] == 'E':
                        self.end = (r,c)
                        self.climbmap[r][c] = 122
                    else:
                        self.climbmap[r][c] = ord(self.climbmap[r][c]) #turn 2D array into ints  
                
    def getFullPath(self):
        self.process()
        
        path = self.findPath(self.climbmap,self.start[0],self.start[1])
        
        return path
    
    def findHikeTrail(self):
        self.process()
        minpath = 1000
        for i in range(len(self.climbmap)):
            for j in range(len(self.climbmap[0])):
                if self.climbmap[i][j] == 97: #start at a
                    path = self.findPath(self.climbmap,i,j)
                    if path > 0:
                        minpath = min(minpath,path)
        return minpath

    # The function returns false if (x, y) is not a valid position
    def isValid(self, x, y, N,M):
        return (0 <= x < N) and (0 <= y < M)
 
    def findPath(self, matrix, x=0, y=0, level=0):
        # base case
        if not matrix or not len(matrix):
            return
     
        N = self.total_rows
        M= self.total_columns
     
        # create a queue and enqueue the first node
        q = deque()     
        q.append((x, y, level))
     
        visited = set()
        visited.add((x, y))
     
        # loop till queue is empty
        while q:
            # dequeue front node and process it
            i, j, level = q.popleft()
     
            # return if the destination is found
            if i == self.end[0] and j == self.end[1]:
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
                if self.isValid(x, y, N,M) and (matrix[x][y] <= matrix[i][j]+1):
                    # if it isn't visited yet
                    
                    if (x, y) not in visited:
                        # construct the next cell node and enqueue it
                        # and mark it as visited
                        q.append((x, y, level + 1))
                        visited.add((x, y))
     
        # return a negative number if the path is not possible
        return -1


import sys

class Cave:
    def __init__(self,p):
        self.input = 'input.txt'
        self.rocks = []
        self.sand = set()
        self.start_sand = (0,500)
        self.full = False
        self.highpoint = 0
        self.left = 1000000
        self.right = 0
        self.problem = p

    def process(self):
        with open(self.input) as f:
            lines = f.readlines()
            for line in lines:
                line=line.strip()
                points = line.split(' -> ')
                start = (-1,-1)
                end = (-1,-1)
                for p in points:
                    c = p.split(',')
                    
                    if start == (-1,-1):
                        start = (int(c[1]),int(c[0]))
                        self.rocks.append(start)
                        if start[0] > self.highpoint:
                            self.highpoint = int(c[1])
                        continue
                    else:
                        end = (int(c[1]),int(c[0]))
                        self.rocks.append(end)
                        if end[0] > self.highpoint:
                            self.highpoint = end[0]
                        if end[1] > self.right:
                            self.right = end[1]
                        if end[1] < self.left:
                            self.left = end[1]

                    if start[0] == end[0]: #same x
                        step = 1 if start[1] < end[1] else -1
                        for i in range(start[1],end[1], step): 
                            self.rocks.append((start[0],i))
                    elif start[1] == end[1]: #same y
                        step = 1 if start[0] < end[0] else -1
                        for i in range(start[0],end[0], step):
                            self.rocks.append((i,start[1]))

                    start = end

    def go1(self):
        self.process()
        self.rocks = set(self.rocks)
        while not self.full:
            self.drop_sand(self.start_sand)
        return len(self.sand)

    def go2(self):
        self.process()
        self.highpoint = self.highpoint + 2
        self.rocks = set(self.rocks)
        while not self.full:
            self.drop_sand(self.start_sand)
        return len(self.sand)
    
    def drop_sand(self,start):
        #print(start)
        if self.problem == 2 and start[0] + 1 >= self.highpoint:
            self.sand.add(start)
            return
        
        if (start[0]+1, start[1]) not in self.rocks and (start[0]+1, start[1]) not in self.sand: #down works
            if self.problem == 1: #problem 1
                done = True
                for x,y in self.rocks:#y position never appears with an x lower than start x then we're done
                    if x>start[0] and y==start[1]:
                        done = False
                if done:
                    self.full = True
                    return
            self.drop_sand((start[0]+1, start[1]))
        elif (start[0]+1, start[1]-1) not in self.rocks and (start[0]+1, start[1]-1) not in self.sand: #left diag
            self.drop_sand((start[0]+1, start[1]-1))
        elif (start[0]+1, start[1]+1) not in self.rocks and (start[0]+1, start[1]+1) not in self.sand: #right diag
            self.drop_sand((start[0]+1, start[1]+1))
        else: #cannot move down
            self.sand.add(start)
            if start == self.start_sand:
                self.full = True
    
                        
                    
            
    

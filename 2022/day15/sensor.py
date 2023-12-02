import math
import gc
from collections import deque
class Sensor:
    def __init__(self,part):
        self.input = 'input.txt'
        self.sensors = set()
        self.beacons = set()
        self.emptypoints = set()
        self.part = part
        self.ranges = [[] for x in range(4000000)]

    def process(self,rowcheck):
        with open(self.input) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                dets = line.split(' ')

                sx = dets[2]
                sx = sx.split('=')
                sx = int(sx[1].strip(','))
                
                sy = dets[3]
                sy = sy.split('=')
                sy = int(sy[1].strip(':'))
                curr_sens = (sx,sy)
                self.sensors.add(curr_sens)

                bx = dets[8]
                bx = bx.split('=')
                bx = int(bx[1].strip(','))
                
                by = dets[9]
                by = by.split('=')
                by = int(by[1].strip(':'))
                curr_beacon = (bx,by)
                self.beacons.add(curr_beacon)

                distance = self.manhattan(curr_sens,curr_beacon)
                if self.part==1:
                    self.shorterpoints(curr_sens, distance,rowcheck)
                else:
                    self.shorterpoints2(curr_sens, distance)

    def go(self,rowcheck):
        self.process(rowcheck)

        if self.part == 2:
            for i in range(len(self.ranges)):
                if len(s.ranges[i])>1:
                    s.ranges[i] = set(s.ranges[i])
                    free =[x for x in [x for x in range(4000000)] if x not in s.ranges[i]]
                    if free:
                        print(i,free)
        
        return len(self.emptypoints)
        
                
    def manhattan(self, start, end):
        return abs(end[0] - start[0]) + abs(end[1]-start[1])

    def shorterpoints(self, start, distance,rowcheck):
        sx = start[0]; sy = start[1]
        max_row = sx + distance; min_row = sx - distance
        max_col = sy + distance; min_col = sy - distance

        for i in range(min_row, max_row+1):
            if self.manhattan(start, (i,rowcheck)) <= distance and (i,rowcheck) not in self.beacons:
                self.emptypoints.add((i,rowcheck))

    def shorterpoints2(self, start, distance):
        sx = start[0]; sy = start[1]
        max_row = min(sx + distance,4000000); min_row = max(sx - distance,0)
        max_col = min(sy + distance,4000000); min_col = max(sy - distance,0)
        

        for i in range(min_row, max_row+1):
            r = distance - abs(sx-i)
            self.ranges[i] = self.ranges[i] + [x for x in range(max(sy - r,min_col), min(sy + r +1,max_col))]
            gc.collect()
        
                


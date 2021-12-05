class VentTracker:
    def __init__(self):
        self.vents_file = 'vents.txt'
        self.vents = [[]]
        
    def getvents(self, diag):
        with open(self.vents_file) as f:
            lines = f.readlines() # list containing lines of file
            c=0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                positions = line.split(' -> ')
                point1 = positions[0].split(',')
                point2 = positions[1].split(',')
                    
                curr_vent = Vent(point1[0], point1[1], point2[0], point2[1])
                curr_vent.fillPoints(diag)
                self.vents.append(curr_vent)
                

    def getoverlaps(self):
        self.getvents(False)
        ventmap = {}
        for v in self.vents:
            if v:
                for p in v.points:
                    if str(p) in ventmap:
                        ventmap[str(p)] = ventmap[str(p)] + 1
                    else:
                        ventmap[str(p)] = 1

        overlap_count = 0
        for m in ventmap.values():
            if m >= 2:
                overlap_count = overlap_count + 1

        return overlap_count

    def getoverlaps2(self):
        self.getvents(True)
        ventmap = {}
        for v in self.vents:
            if v:
                for p in v.points:
                    if str(p) in ventmap:
                        ventmap[str(p)] = ventmap[str(p)] + 1
                    else:
                        ventmap[str(p)] = 1

        overlap_count = 0
        for m in ventmap.values():
            if m >= 2:
                overlap_count = overlap_count + 1

        return overlap_count
        
class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
        self.points = []
        self.slope = self.calc_slope(int(x1),int(y1),int(x2),int(y2))
    
    def fillPoints(self, include_diag):
        if self.x1 == self.x2:
            y_start = min(self.y1,self.y2)
            y_end = max(self.y1,self.y2)
            for i in range(y_start, y_end+1):
                p = (self.x1, i)

                if p not in self.points:
                    self.points.append(p)

        elif self.y1 == self.y2:
            x_start = min(self.x1,self.x2)
            x_end = max(self.x1,self.x2)
            for i in range(x_start, x_end+1):
                p = (i, self.y1)

                if p not in self.points:
                    self.points.append(p)
        if include_diag:
            if self.slope == 1:
                
                pos_x_start = 0
                pos_y_start = 0
                pos_x_end = 0
                pos_y_end = 0
                if self.x1 < self.x2:
                    pos_x_start = self.x1
                    pos_y_start = self.y1
                    pos_x_end = self.x2
                    pos_y_end = self.y2
                else:
                    pos_x_start = self.x2
                    pos_y_start = self.y2
                    pos_x_end = self.x1
                    pos_y_end = self.y1

                while pos_x_start <= pos_x_end:
                    p = (pos_x_start, pos_y_start)
                    if p not in self.points:
                        self.points.append(p)

                    if pos_y_start < pos_y_end:
                        pos_y_start = pos_y_start + 1
                    else:
                        pos_y_start = pos_y_start - 1
                
                    pos_x_start = pos_x_start + 1
                
    def calc_slope(self, x1, y1, x2, y2):
        rise = abs(y1-y2)
        run = abs(x1-x2)
        
        if rise == 0 or run == 0:
            return 0
        else:
            return rise/run

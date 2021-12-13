import matplotlib.pyplot as plt
import numpy as np

class Origami:
    def __init__(self):
        self.manual = 'manual.txt'
        self.points = []
        self.instructions = []

    def getManual(self):
        with open(self.manual) as f:
            for line in f:
                value = line.strip().split(',')
                if len(value) == 2: #is a point
                    self.points.append([int(value[0]), int(value[1])])
                elif value != ['']: #is instruction
                    ins_set = value[0].split(' ')
                    ins_val = ins_set[2].split('=')
                    self.instructions.append([ins_val[0], int(ins_val[1])])
                        
    def makeShape1(self):
        self.getManual()
        self.fold(self.instructions[0][0], self.instructions[0][1])
        return self.countUnique()

    def makeShape2(self):
        self.getManual()
        for i in self.instructions:
            self.fold(i[0], i[1])
        
        x = np.array([p[0] for p in self.points])
        y = np.array([p[1] for p in self.points])

        plt.scatter(x, y)
        plt.show() #upside down image, need to flip over the y axis but it was readable

    def countUnique(self):
        unique_points = []
        for p in self.points:
            if p not in unique_points:
                unique_points.append(p)
        return len(unique_points)

    def fold(self, axis, line):
        num_points = len(self.points)
        if axis == 'x':
            for p in range(0, num_points):
                if self.points[p][0] > line:
                    new_x = line - (self.points[p][0] - line)
                    self.points[p][0] = new_x
        if axis == 'y':
            for p in range(0, num_points):
                if self.points[p][1] > line:
                    new_y = line - (self.points[p][1] - line)
                    self.points[p][1] = new_y

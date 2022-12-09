import numpy
class Rope:
    def __init__(self):
        self.input_file = 'input.txt'
        self.tailpath = [(0,0)]
        self.head_pos = (0,0)
        self.tail_pos = (0,0)
        self.all_tail_pos = [(0,0) for x in range(0,9)]

        
    def process(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            
            for line in lines:
                line = line.strip()
                ins = line.split(' ')
                self.move(ins[0],int(ins[1]))
        print(len(set(self.tailpath)))

    def new_spot(self, front, back):
        x = 0
        y = 0
        if front[0] > back[0]:
            x=1
        elif front[0] < back[0]:
            x=-1

        if front[1]>back[1]:
            y=1
        elif front[1]<back[1]:
            y=-1
        return(x,y)

    def move(self, direction, count):
        #print(self.head_pos)
        #print(self.all_tail_pos)
        #print('---')
        if direction == 'R':
            for i in range(0,count):
                self.head_pos = (self.head_pos[0],self.head_pos[1]+1)
                front = self.head_pos
                for t in range(0,9):
                    back = self.all_tail_pos[t]
                    if self.needs_move(front,back):
                        move = self.new_spot(front, back)
                        self.all_tail_pos[t] = (back[0]+move[0],back[1]+move[1])
                        if t == 8:
                            self.tailpath.append(self.all_tail_pos[t])
                    front = self.all_tail_pos[t]
                    
        elif direction == 'L':
            for i in range(0,count):
                self.head_pos = (self.head_pos[0],self.head_pos[1]-1)
                front = self.head_pos
                for t in range(0,9):
                    back = self.all_tail_pos[t]
                    if self.needs_move(front,back):
                        move = self.new_spot(front, back)
                        self.all_tail_pos[t] = (back[0]+move[0],back[1]+move[1])
                        if t == 8:  
                            self.tailpath.append(self.all_tail_pos[t])
                    front = self.all_tail_pos[t]

        elif direction == 'U':
            for i in range(0,count):
                self.head_pos = (self.head_pos[0]+1,self.head_pos[1])
                front = self.head_pos
                for t in range(0,9):
                    back = self.all_tail_pos[t]
                    if self.needs_move(front,back):
                        move = self.new_spot(front, back)
                        self.all_tail_pos[t] = (back[0]+move[0],back[1]+move[1])
                        if t == 8:
                            self.tailpath.append(self.all_tail_pos[t])
                    front = self.all_tail_pos[t]

        elif direction == 'D':
            for i in range(0,count):
                self.head_pos = (self.head_pos[0]-1,self.head_pos[1])
                front = self.head_pos
                for t in range(0,9):
                    back = self.all_tail_pos[t]
                    if self.needs_move(front,back):
                        move = self.new_spot(front, back)
                        self.all_tail_pos[t] = (back[0]+move[0],back[1]+move[1])
                        if t == 8:
                            self.tailpath.append(self.all_tail_pos[t])
                    front = self.all_tail_pos[t]
        return

    def needs_move(self, front, back):
        if abs(front[0] - back[0]) > 1 or abs(front[1]-back[1]) > 1:
            return True
        return False
            
                

                
            


                

    

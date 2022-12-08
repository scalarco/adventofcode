import numpy
class TreeTop:
    def __init__(self):
        self.input_file = 'input.txt'
        self.rows = [[]]
        self.cols = [[]]
        
    def process(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            self.rows = [[] for x in range(0,len(lines))]
            self.cols = [[] for x in range(0,len(lines[0])-1)]
            curr_row = 0
            for line in lines:
                line = line.strip()
                
                for i in range(0, len(line)):
                    self.rows[curr_row].append(int(line[i]))
                    self.cols[i].append(int(line[i]))
                curr_row = curr_row + 1

    def countvis(self):
        count = 0
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.cols)):
                if self.is_vis(i,j):
                    count=count+1
        return count

    def maxh(self, val):
        if val:
            return max(val)
        return 0
        
    def is_vis(self, x, y):
        
        val = self.rows[x][y]
        if x == len(self.rows)-1 or x == 0:
            return True
        if y == len(self.cols)-1 or y == 0:
            return True
        
        if val > self.maxh(self.rows[x][0:y]) or val > self.maxh(self.rows[x][y+1:]) or val > self.maxh(self.cols[y][0:x]) or val > self.maxh(self.cols[y][x+1:]):
                return True
        return False

    def max_score(self):
        total = 0
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.cols)):
                curr_score = self.scenic_score(i,j)
                if curr_score > total:
                    total=curr_score
        return total
    
    def scenic_score(self, x, y):
        scores=[0,0,0,0] #L,R,U,D
        val = self.rows[x][y]
        #left
        if y > 0:
            j = y - 1
            lastheight = -1
            while j >= 0:
                currheight = self.rows[x][j]
                if currheight < val:
                    scores[0] = scores[0] + 1
                    lastheight = currheight
                else:
                    scores[0] = scores[0] + 1
                    break
                j = j-1
        #right
        if y < len(self.cols)-1:
            j = y + 1
            lastheight = -1
            while j < len(self.cols):
                currheight = self.rows[x][j]
                if currheight < val:
                    scores[1] = scores[1] + 1
                    lastheight = currheight
                else:
                    scores[1] = scores[1] + 1
                    break
                j = j+1
        #up
        
        if x > 0:
            j = x - 1
            lastheight = -1
            while j >= 0:
                currheight = self.rows[j][y]
                if currheight < val:
                    scores[2] = scores[2] + 1
                    lastheight = currheight
                else:
                    scores[2] = scores[2] + 1
                    break
                j = j-1
        #down
        if x < len(self.rows)-1:
            j = x + 1
            lastheight = -1

            while j < len(self.rows):
                currheight = self.rows[j][y]
                if currheight<val:
                    scores[3] = scores[3] + 1
                    lastheight = currheight
                else:
                    scores[3] = scores[3] + 1
                    break
                j = j+1

        return numpy.prod(scores)
            
            
                

                
            


                

    

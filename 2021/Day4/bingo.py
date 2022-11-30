import json
                
class BingoGame:
    def __init__(self):
        self.prizes_drawn = [27,14,70,7,85,66,65,57,68,23,33,78,4,84,25,18,43,71,76,61,34,82,93,74,26,15,83,64,2,35,19,97,32,47,6,51,99,20,77,75,56,73,80,86,55,36,13,95,52,63,79,72,9,10,16,8,69,11,50,54,81,22,45,1,12,88,44,17,62,0,96,94,31,90,39,92,37,40,5,98,24,38,46,21,30,49,41,87,91,60,48,29,59,89,3,42,58,53,67,28]
        self.boards_file = 'boards.txt'
        self.boards = [[]]

    def getBoards(self):
        with open(self.boards_file) as f:
            lines = f.readlines() # list containing lines of file

            l = 1
            
            curr_rows = [[]] * 5
            curr_columns = [[]] * 5
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if l % 6 == 0:
                    curr_board = Board(curr_rows, curr_columns)
                    self.boards.append(curr_board)

                    curr_rows = [[]] * 5
                    curr_columns = [[]] * 5
                else:
                    values = line.split(' ')
                    try:
                        while True:
                            values.remove('')
                    except ValueError:
                        pass

                    for v in range(0, len(values)):
                        curr_rows[(l%6)-1] = curr_rows[(l%6)-1] + [(int(values[v]), 0)]
                        curr_columns[v] = curr_columns[v] + [(int(values[v]), 0)]
                l = l + 1
        
    def playGame1(self):
        self.getBoards()
        for p in self.prizes_drawn:
            for b in self.boards:
                if b:
                    b.mark(p)
                    if b.checkWin():
                        board_sum = b.getSumUnmarked()
                        return board_sum * p
        return 0

    def playGame2(self):
        self.getBoards()
        last_winner_sum = 0
        for p in self.prizes_drawn:
            for b in self.boards[:]:
                if b:
                    b.mark(p)
                    if b.checkWin():
                        last_winner_sum = b.getSumUnmarked() * p
                        self.boards.remove(b)

        return last_winner_sum 

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
    def mark(self, number):
        for r in self.rows:
            for v in range(0,len(r)):
                itemlist = list(r[v])
                if int(itemlist[0]) == number:
                    itemlist[1] = 1
                item = tuple(itemlist)
                r[v] = item
                    
        for c in self.columns:
            for v in range(0,len(c)):
                itemlist = list(c[v])
                if int(itemlist[0]) == number:
                    itemlist[1] = 1
                item = tuple(itemlist)
                c[v] = item

    def checkWin(self):
        for r in self.rows:
            row_win = True
            for v in r:
                    if v[1] == 0:
                        row_win = False
                        break
            if row_win == True:
                return True
                
        for c in self.columns:
            col_win = True
            for v in c:
                if v[1] == 0:
                    col_win = False
                    break
            if col_win == True:
                return True
        return False

    def getSumUnmarked(self):
        result = 0
        for r in self.rows:
            for v in r:
                if v[1] == 0:
                    result = result + v[0]
        return result
    

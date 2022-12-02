class RPS:
    def __init__(self):
        self.strategy_file = 'strategy.txt'
        self.scores = {
            ('A','X'): 4,
            ('A','Y'): 8,
            ('A','Z'): 3,
            ('B','X'): 1,
            ('B','Y'): 5,
            ('B','Z'): 9,
            ('C','X'): 7,
            ('C','Y'): 2,
            ('C','Z'): 6
        }
        self.outcomes = {
            ('A','X'): 3, #choose Z
            ('A','Y'): 4, #choose X
            ('A','Z'): 8, #choose Y
            ('B','X'): 1, #choose X
            ('B','Y'): 5, #choose Y
            ('B','Z'): 9, #choose Z
            ('C','X'): 2, #choose Y
            ('C','Y'): 6, #choose Z
            ('C','Z'): 7 #choose X
        }
        
    def getstrategy(self):
        with open(self.strategy_file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                plays = line.split(' ')
                score = self.scores[(plays[0], plays[1])]
                total = total + score
            return total
    def getoutcomes(self):
        with open(self.strategy_file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                plays = line.split(' ')
                score = self.outcomes[(plays[0], plays[1])]
                total = total + score
            return total
    

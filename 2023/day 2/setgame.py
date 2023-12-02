class SetGame:
    def __init__(self):
        self.file = 'codes.txt'
        self.codes = []
        self.maxred = 12
        self.maxgreen = 13
        self.maxblue = 14
        
    def gettotal(self):
        with open(self.file) as f:
            lines = f.readlines() # list containing lines of file
            validsum = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if line:
                    game = line.split(':')
                    gamenum = game[0].split(' ')[1]
                    sets = game[1].split(';')
                    validround = True
                    for s in sets:
                        items = s.split(',')
                        for i in items:
                            i = i.split(' ')
                            
                            if i[2] == 'red' and int(i[1]) > self.maxred:
                                
                                validround = False
                                break
                            if i[2] == 'blue' and int(i[1]) > self.maxblue:
                                
                                validround = False
                                break
                            if i[2] == 'green' and int(i[1]) > self.maxgreen:
                                
                                validround = False
                                break
                        if not validround:
                            break
                    if validround:
                        
                        validsum = validsum + int(gamenum)
            return validsum

    def gettotal2(self):
        with open(self.file) as f:
            lines = f.readlines() # list containing lines of file
            sumpower = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if line:
                    game = line.split(':')
                    gamenum = game[0].split(' ')[1]
                    sets = game[1].split(';')
                    roundpower = 0
                    minred = 0
                    mingreen = 0
                    minblue = 0
                    for s in sets:
                        items = s.split(',')
                        for i in items:
                            i = i.split(' ')
                            
                            if i[2] == 'red':
                                minred = max(minred, int(i[1]))               
                            elif i[2] == 'blue':
                                minblue = max(minblue, int(i[1]))  
                            elif i[2] == 'green':
                                mingreen = max(mingreen, int(i[1]))
                    roundpower = minred * minblue * mingreen
                    sumpower = sumpower + roundpower
            return sumpower
                                                              
                                

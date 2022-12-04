class Ranges:
    def __init__(self):
        self.input_file = 'input.txt'
        
    def getfulloverlaps(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                ranges = line.split(',')
                range1 = ranges[0].split('-')
                range2 = ranges[1].split('-')
                if int(range1[0])<=int(range2[0]) and int(range1[1])>=int(range2[1]): #1 encaps 2
                    total = total + 1
                    
                elif int(range2[0])<=int(range1[0]) and int(range2[1])>=int(range1[1]): #2 encaps 1
                    total = total + 1
                    
            return total

    def getpartialoverlaps(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                ranges = line.split(',')
                range1 = ranges[0].split('-')
                range2 = ranges[1].split('-')
                if int(range1[0]) <= int(range2[0]) <= int(range1[1]):
                    total = total + 1   
                elif int(range1[0]) <= int(range2[1]) <= int(range1[1]):
                    total = total + 1
                elif int(range2[0]) <= int(range1[0]) <= int(range2[1]):
                    total = total + 1   
                elif int(range2[0]) <= int(range1[1]) <= int(range2[1]):
                    total = total + 1
                    
            return total

                

    

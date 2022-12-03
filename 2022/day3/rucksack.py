class RIC:
    def __init__(self):
        self.input_file = 'input.txt'
        
    def getsacks(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                size = int(len(line)/2)
                half_one = line[0:size]
                half_two = line[size:]
                common_char = list(set(half_one).intersection(half_two))[0]
                if ord(common_char)-96 > 0:
                    total = total + ord(common_char)-96
                else:
                    total = total + ord(common_char)-38
            return total
    def get3sacks(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            
            line_sets = []
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if len(line_sets) < 2:
                    line_sets.append(line)
                else:
                    line_sets.append(line)
                    common_char = list(set(line_sets[0]).intersection(line_sets[1]).intersection(line_sets[2]))[0]
                    if ord(common_char)-96 > 0:
                        total = total + ord(common_char)-96
                    else:
                        total = total + ord(common_char)-38
                    line_sets = []
            return total

                

    

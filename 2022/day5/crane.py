import re
class Crane:
    def __init__(self):
        self.input_file = 'input.txt'
        self.instructions = []
        self.configs = [[] for x in range(0,9)]
        
        
    def getconfig(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            
            is_config = True
            for line in lines:
                if not line[0] == '[':
                    is_config = False
                    
                if is_config:
                    counter = 0
                    i = 0
                    while i < len(line):
                        if line[i] == '[':
                            curr_val = line[i+1]
                            curr_index = counter
                            self.configs[curr_index].append(curr_val)
                            counter = counter+1
                            i = i + 3 #end of value
                        elif line[i] == ' ' and not line[i+1] == ' ':
                            i = i+1
                        elif line[i] == ' ' and line[i+1] == ' ':
                            counter = counter + 1
                            i = i + 4
                        else:
                            i = i + 1
                        
                else:
                    if line[0] == 'm':
                        line = line.strip()
                        self.instructions.append(line)

    def apply_instructions_9000(self):
        for ins in self.instructions:
            details = re.split(r'\D+',ins)
            from_col = int(details[2]) - 1
            to_col = int(details[3]) - 1
            for i in range(0, int(details[1])):
                curr_move = self.configs[from_col].pop(0)
                self.configs[to_col].insert(0, curr_move)

    def apply_instructions_9001(self):
        for ins in self.instructions:
            details = re.split(r'\D+',ins)
            curr_set_move = []
            from_col = int(details[2]) - 1
            to_col = int(details[3]) - 1
            for i in range(0, int(details[1])):
                curr_move = self.configs[from_col].pop(0)
                curr_set_move.append(curr_move)

            self.configs[to_col] = curr_set_move + self.configs[to_col]
                
            


                

    

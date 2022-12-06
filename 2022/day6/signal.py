import re
class SigCheck:
    def __init__(self):
        self.input_file = 'input.txt'
        
        
    def process(self, size):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
             
            unique_set = []
            visited_count = 0
            for line in lines:
                line = line.strip()
                
                for i in range(0,len(line)):
                    curr_char = line[i]
                    visited_count = visited_count + 1
                    
                    if curr_char not in unique_set:
                        unique_set.append(curr_char)
                    else:
                        pos = unique_set.index(curr_char)    
                        unique_set = unique_set[pos+1:] + [curr_char]
                    
                    if len(unique_set) == size:
                        break
                    
            return visited_count
                

                
            


                

    

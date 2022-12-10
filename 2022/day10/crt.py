import numpy
class CRT:
    def __init__(self):
        self.input_file = 'input.txt'
        self.cpu_x = 1
        self.cycle = 1
        self.sumcycles=[20,60,100,140,180,220]
        self.image = ''
        self.rowlen = 40
        
    def should_draw(self,cpu,currpix):
        if cpu-1<=currpix<=cpu+1:
            return True
        return False
        
    def process(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file

            sum_sig=0
            
            for line in lines:
                line = line.strip()
                ins = line.split(' ')

                
                if ins[0] == 'noop':
                    if self.should_draw(self.cpu_x,(self.cycle-1)%40):
                        self.image = self.image + '#'
                    else:
                        self.image = self.image + '.'
                    if self.cycle in self.sumcycles:
                        sum_sig = sum_sig + (self.cycle * self.cpu_x)
                    self.cycle = self.cycle+1
                elif ins[0] == 'addx':

                    if self.should_draw(self.cpu_x,(self.cycle-1)%40):
                        self.image = self.image + '#'
                    else:
                        self.image = self.image + '.'

                    if self.cycle in self.sumcycles:
                        sum_sig = sum_sig + (self.cycle * self.cpu_x)

                    self.cycle = self.cycle+1


                    if self.should_draw(self.cpu_x,(self.cycle-1)%40):
                        self.image = self.image + '#'
                    else:
                        self.image = self.image + '.'

                    if self.cycle in self.sumcycles:
                        sum_sig = sum_sig + (self.cycle * self.cpu_x)

                    self.cycle = self.cycle+1

                    self.cpu_x = self.cpu_x + int(ins[1])
            self.print_image()
            return sum_sig

    def print_image(self):
        temp = ''
        for i in range(0, len(self.image)):
            if i%40==0:
                print(temp)
                temp=''
            temp = temp + self.image[i]
        print(temp)

                    


    
            
                

                
            


                

    

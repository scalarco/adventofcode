import ast
from functools import cmp_to_key
class Pairs:
    def __init__(self):
        self.input_file = 'input.txt'
        self.packets = []
         
    def go(self):
        self.packets.append([[2]])
        self.packets.append([[6]])
        self.process()
        p = sorted(self.packets,key=cmp_to_key(self.compare))
        div1 = 0
        div2 = 0
        for i in range(len(p)):
            if p[i] == [[2]]:
                div1 = i+1
            if p[i] == [[6]]:
                div2 = i+1
        return div1*div2

    def compare(self, a, b):
        val1 = a
        val2 = b
        x = 0
        sizea = 1
        sizeb = 1

        if not a and b:
            return -1
        elif not b and a:
            return 1
        elif not b and not a:
            return 0
        
        if type(a) == list:
            val1 = a[0]
            sizea = len(a)
        if type(b) == list:
            val2 = b[0]
            sizeb = len(b)

        if type(val1) == int and type(val2) == int:
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
            else:
                if sizea > 1 and sizeb > 1:
                    x = self.compare(a[1:],b[1:])
                elif sizea > 1:
                    return 1
                elif sizeb > 1:
                    return -1
                else:
                    return 0    
        else:
            if type(val1) == int:
                val1 = [val1]
            if type(val2) == int:
                val2 = [val2]
            
            x = self.compare(val1,val2)

        if x==-1:
            return -1
        elif x == 1:
            return 1
        
        if sizea > 1 and sizeb > 1:
            return self.compare(a[1:],b[1:])
        elif sizea > 1:
            return 1
        elif sizeb > 1:
            return -1
        
        return x    
                
        
    def process(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            a = []
            b = []
            count = 0
            
            pair_evals = []
            for line in lines:
                line = line.strip()
                if not line:
                    pair_evals.append(self.compare(a,b))
                    count = 0
                    continue
                
                if count == 0:
                    a = ast.literal_eval(line)
                    self.packets.append(a)
                    count = count +1
                elif count == 1:
                    b = ast.literal_eval(line)
                    self.packets.append(b)
                    count = count +1
            pair_evals.append(self.compare(a,b))
            count = 0
            print(pair_evals)
            sump = 0
            for i in range(len(pair_evals)):
                if pair_evals[i] == -1:
                    sump = sump + i + 1
            return sump

                    
                



    
            
                

                
            


                

    

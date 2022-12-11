import math
from functools import reduce
class MonSim:
    def __init__(self):
        self.input_file = 'input.txt'
        self.monkeys = []
        self.divisors = []
        self.lcm_val = 0
        
    def print_monkeys(self):
        for m in self.monkeys:
            m.printm()

    
    def lcm(self,arr):
        l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
        return l
    
    def go(self,rounds):
        self.process()
        self.lcm_val = self.lcm(self.divisors)
        for i in range(0,rounds):
            self.run_round()
        self.print_monkeys()
        top1 = 0
        top2 = 0
        for m in self.monkeys:
            if m.inspection_count>top1:
                top1=m.inspection_count
            elif m.inspection_count>top2:
                top2=m.inspection_count
        return top1*top2
        
    def process(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
            curr_monkey = 0
            curr_items = []
            curr_ops = None
            curr_testval = None
            curr_targettrue = None
            curr_targetfalse = None
            for line in lines:
                line = line.strip()
                lps = line.split(' ')
                if lps[0] == 'Monkey':
                    curr_monkey = int(lps[1].strip(':'))
                elif lps[0] == 'Starting':
                    for i in lps[2:]:
                        curr_items.append(int(i.strip(',')))
                elif lps[0] == 'Operation:':
                    curr_ops = (lps[3],lps[4],lps[5])
                elif lps[0] == 'Test:':
                    curr_testval = int(lps[3])
                    self.divisors.append(int(lps[3]))
                elif lps[0] == 'If' and lps[1] == 'true:':
                    curr_targettrue = int(lps[5])
                elif lps[0] == 'If' and lps[1] == 'false:':
                    curr_targetfalse = int(lps[5])
                else:
                    new_monkey = Monkey(curr_monkey,curr_items,curr_ops,curr_testval,curr_targettrue,curr_targetfalse)
                    self.monkeys.append(new_monkey)
                    curr_monkey = curr_monkey+1
                    curr_items = []
                    curr_ops = None
                    curr_testval = None
                    curr_targettrue = None
                    curr_targetfalse = None
            new_monkey = Monkey(curr_monkey,curr_items,curr_ops,curr_testval,curr_targettrue,curr_targetfalse)
            self.monkeys.append(new_monkey)

    def run_round(self):
        
        for m in self.monkeys:

            for i in range(0,len(m.items)):
                m.inspection_count = m.inspection_count + 1
                m.items[i] = m.operation(m.items[i]) #op
                #m.items[i] = int(m.items[i] / 3) #bored relief part 1
                m.items[i] = int(m.items[i] % self.lcm_val) #bored relief part 2
                if m.test(m.items[i]):
                    self.monkeys[m.targettrue].add_item(m.items[i]) #add to other monkey
                else:
                    self.monkeys[m.targetfalse].add_item(m.items[i]) #add to other monkey
            m.items = [] #reset item list to empty
                    
                

class Monkey:
    def __init__(self,num,items,operators,testval,targettrue,targetfalse):
        self.num = num
        self.items = items
        self.testval = testval
        self.targettrue = targettrue
        self.targetfalse = targetfalse
        self.operators = operators
        self.inspection_count = 0
        
    def test(self,item):
        return item % int(self.testval) == 0
        
    def printm(self):
        print(self.num)
        print(self.items)
        print(self.testval)
        print(self.targettrue)
        print(self.targetfalse)
        print(self.operators)
        print(self.inspection_count)
        print('---')
        
    def add_item(self,item):
        self.items.append(item)

    
    def operation(self,item):
        op = self.operators[1]
        x1 = self.operators[0]
        if x1 == 'old':
            x1=item
        x2 = self.operators[2]
        if x2 == 'old':
            x2=item
            
        if op == '+':
            return int(x1)+int(x2)
        elif op == '-':
            return int(x1)-int(x2)
        elif op == '*':
            return int(x1)*int(x2)
        elif op == '/':
            return int(x1)/int(x2)


    
            
                

                
            


                

    

from collections import Counter
class PolymerSim:
    def __init__(self):
        self.manual = 'polymer.txt'
        self.template = ''
        self.insertions = {}

    def getManual(self):
        with open(self.manual) as f:
            for line in f:
                value = line.strip().split(' -> ')
                if len(value) == 1 and value != ['']: #is template
                    self.template = value[0]
                elif value != ['']: #is insertion
                    self.insertions[value[0]] = value[1]

    def simPolymer(self, steps):
        self.getManual()

        for i in range(0,steps): #10 steps

            step_p = self.template
            for j in range(0, len(step_p)-1):
                curr_pair = step_p[j] + step_p[j+1]
                ins_char = self.insertions[curr_pair]
                if j == 0:
                    self.template = step_p[j] + ins_char + step_p[j+1]
                else:
                    self.template = self.template + ins_char + step_p[j+1]        

        occurances = Counter(self.template)
        max_o = max(occurances, key=occurances.get)
        min_o = min(occurances, key=occurances.get)
        return occurances[max_o] - occurances[min_o]

    def effPolymer(self, steps): #efficient polymer sim using dict of pairs
        self.getManual()

        pairs = {}
        last_char = self.template[-1:]
        for j in range(0, len(self.template)-1):
            curr_pair = self.template[j] + self.template[j+1]
            if curr_pair in pairs:
                pairs[curr_pair] = pairs[curr_pair] + 1
            else:
                pairs[curr_pair] = 1
                
        for i in range(0,steps): #10 steps
            add_pairs = {}
            for p in pairs:
                ins_char = self.insertions[p]
                if p[0] + ins_char in add_pairs:
                    add_pairs[p[0] + ins_char] = add_pairs[p[0] + ins_char] + pairs[p]
                else:
                    add_pairs[p[0] + ins_char]=pairs[p]
                if ins_char + p[1] in add_pairs:
                    add_pairs[ins_char + p[1]] = add_pairs[ins_char + p[1]] + pairs[p]
                else:
                    add_pairs[ins_char + p[1]]=pairs[p]
            pairs = add_pairs    

        countdict = {}
        for p in pairs:
            if p[0] in countdict:
                countdict[p[0]] = countdict[p[0]] + pairs[p]
            else:
                countdict[p[0]] = pairs[p]

        countdict[last_char] = countdict[last_char] + 1
        max_o = max(countdict, key=countdict.get)
        min_o = min(countdict, key=countdict.get)
        return countdict[max_o] - countdict[min_o]

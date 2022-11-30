class SegSearch:
    def __init__(self, days=80):
        self.wires_file = 'wires.txt'
        self.displays = {}
        
    def getwires(self):
        with open(self.wires_file) as f:
            lines = f.readlines() # list containing lines of file

            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                curr_wires = line.split('|')
                self.displays[curr_wires[0].strip()] = curr_wires[1].strip()

    def getunique(self):
        self.getwires()
        unique_count = 0
        unique_lengths = [2,4,3,7]

        for v in self.displays.values():
            numbers = v.split(' ')
            for n in numbers:
                if len(n) in unique_lengths:
                    unique_count = unique_count + 1
        return unique_count

    #This function is embarassing but whatever it works
    def getall(self):
        self.getwires()
        unique_count = 0
        unique_lengths = [2,4,3,7]
        total_sum = 0

        for v in self.displays.keys():
            segments = {}
            numbers = v.split(' ')
            current_digits = self.displays[v].split(' ')
            
            for i in numbers:
                if len(i) == 2:
                    segments['1'] = i
                elif len(i)== 3:
                    segments['7'] = i
                elif len(i) == 4:
                    segments['4'] = i
                elif len(i) == 7:
                    segments['8'] = i

            for n in numbers:
                if len(n) == 5:
                        flag=True
                        for i in segments['1']:
                                if i not in n:
                                        flag=False
                        if flag:
                                segments['3'] = n
            for n in numbers:
                if len(n) == 6:
                        flag=True
                        for i in segments['4']:
                                if i not in n:
                                        flag=False
                        if flag:
                                segments['9'] = n
            for n in numbers:
                if len(n) == 6 and n!= segments['9']:
                        flag=True
                        for i in segments['1']:
                                if i not in n:
                                        flag=False
                        if flag:
                                segments['0'] = n

            for n in numbers:
                if len(n) == 6 and n!= segments['9'] and n!= segments['0']:
                    segments['6'] = n

            for n in numbers:
                if len(n) == 5 and n != segments['3']:
                        flag=True
                        for i in n:
                                if i not in segments['9']:
                                        flag=False
                        if flag:
                                segments['5'] = n

            for n in numbers:
                if len(n) == 5 and n != segments['3'] and n != segments['5']:
                    segments['2'] = n

            display_val = ''
            
            for d in current_digits:
                dis = [mapped for mapped,code in segments.items() if sorted(code) == sorted(d)]
                display_val = display_val + dis[0]
            total_sum = total_sum + int(display_val)
        return total_sum

                

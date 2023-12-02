class Decoder:
    def __init__(self):
        self.file = 'codes.txt'
        self.codes = []
        self.nummap = [
            'one' , '1',
            'two' , '2',
            'three' , '3',
            'four' ,'4',
            'five' ,'5',
            'six' , '6',
            'seven' , '7',
            'eight' , '8',
            'nine' , '9'
            ]
        self.tr = {
            'one' : '1',
            'two' : '2',
            'three' : '3',
            'four' :'4',
            'five' :'5',
            'six' : '6',
            'seven' : '7',
            'eight' : '8',
            'nine' : '9'
            }
    def gettotal(self):
        with open(self.file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if line:
                    self.codes.append(line)
                    fn = 0
                    ln = 0
                    for a in range(0,len(line)):
                        if fn==0 and line[a].isnumeric():
                            fn=line[a]
                            ln=line[a]
                        elif line[a].isnumeric():
                            ln=line[a]
                total = total + int(fn+ln)
            return total

    def gettotal3(self):
         with open(self.file) as f:
            lines = f.readlines() # list containing lines of file
            total = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if line:
                    total = total + self.help(line)
            return total

    def help(self,line):
        fn=0
        fd = False
        ln=0
        ld = False
        for x in range(1,len(line)+1):
            start=line[0:x]
            end = line[-x:]
            
            for v in self.nummap:
                
                if not fd and v in start:
                    fn=v
                    fd = True
                if not ld and v in end:
                    ln=v
                    ld= True
        if fn in self.tr:
            fn=self.tr[fn]
        if ln in self.tr:
            ln=self.tr[ln]
        return int(fn+ln)
                                
                                

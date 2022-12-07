import re
class DirSize:
    def __init__(self):
        self.input_file = 'input.txt'
        self.directories = []
        self.disksize = 70000000
        self.updatesize = 30000000
        self.used = 0
        
        
    def process(self):
        with open(self.input_file) as f:
            lines = f.readlines() # list containing lines of file
             
            curr_dir = None
            for line in lines:
                line = line.strip()
                elems = line.split(' ')
                if elems[0] == '$': #command
                    comm = elems[1]
                    if comm == 'cd':
                        if elems[2] == '..':
                            curr_dir.parent.size = curr_dir.parent.size + curr_dir.size
                            curr_dir = curr_dir.parent
                        else:
                            if not self.find(elems[2], curr_dir):
                                newdir = Directory(elems[2], curr_dir)
                                self.directories.append(newdir)
                                curr_dir = newdir
                            else:
                                curr_dir = self.find(elems[2], curr_dir)
                    if comm == 'ls':
                        continue
                elif elems[0] == 'dir':
                    continue
                else: #add file
                    curr_dir.add(elems[1], elems[0])
                    self.used = self.used + int(elems[0])
                    

    def find(self,name,parent):
        for d in self.directories:
            if d.name == name and d.parent == parent:
                return d
        return None

    def getsum(self,value = 100000):
        s = 0
        for a in self.directories:
            if a.size <= value:
                s = s + a.size
        return s

    def getdelsize(self):
        curr_delsize = self.used
        to_free = self.updatesize - (self.disksize - self.used)
        for a in self.directories:
            if a.size > to_free and a.size < curr_delsize:
                curr_delsize = a.size
        return curr_delsize

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = []
        
    def add(self, name, val):
        if name not in self.files:
            self.files.append(name)
            self.size = self.size + int(val)
    def printdet(self):
        p = self.parent.name if self.parent else ''
        print(self.name + ': ' + str(self.size) + ',parent: ' + p)
                    
            
                

                
            


                

    

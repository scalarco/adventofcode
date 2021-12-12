import os
class CavePath:
    def __init__(self):
        self.cavemap_file = 'cavemap.txt'
        self.caves = {}
        self.rawpaths = []

    def getCavemap(self):
        cavenames = {}
        with open(self.cavemap_file) as f:
            for line in f:
                path = line.strip().split('-')

                if path[0] not in cavenames:
                    if path[0].isupper():
                        cs = Cave(path[0], 1)
                    else:
                        cs = Cave(path[0], 0)
                    cavenames[path[0]] = cs
                if path[1] not in cavenames:
                    if path[1].isupper():
                        cd = Cave(path[1], 1)
                    else:
                        cd = Cave(path[1], 0)
                    cavenames[path[1]] = cd
                cavenames[path[0]].addNeighbor(cavenames[path[1]])
                cavenames[path[1]].addNeighbor(cavenames[path[0]])
        self.caves = cavenames

    def traverseCave(self):
        self.getCavemap()

        start = self.caves['start']
        return self.findpath(start, 0, [])

    def traverseCave2(self):
        self.getCavemap()

        start = self.caves['start']
        
        self.findpath2(start, 0, {}, None,[])
        return len(self.rawpaths)

    def findpath(self, start, complete_path, visited_smalls):
        if start.name == 'end':
            complete_path = complete_path + 1
            return complete_path

        if start.size == 0 and start.name not in visited_smalls:
            visited_smalls.append(start.name)

        for n in start.neighbors:
            if n.name not in visited_smalls:
                complete_path = self.findpath(n, complete_path, visited_smalls)
        if start.name in visited_smalls:
            visited_smalls.remove(start.name)
            
        return complete_path

    def checkhas2(self, path):
        curr_dict = {}
        for a in path:
            if not a.isupper():
                if a in curr_dict:
                    curr_dict[a] = curr_dict[a] + 1
                else:
                    curr_dict[a] = 1
        count2 = 0
        for d in curr_dict.values():
            if d >= 2:
                count2 = count2 + 1
        return (count2 >= 2)
    
    def findpath2(self, start, complete_path, visited_smalls, small2, curr_path): #This method was disgusting, could be cleaned up so much
        curr_path.append(start.name)
        
        if start.name == 'end':
            complete_path = complete_path + 1
            self.rawpaths.append(curr_path)
            
            curr_path.remove('end')
            return self.rawpaths

        if start.size == 0 and start.name != 'start':
            if start.name not in visited_smalls:
                visited_smalls[start.name] = 1
            else:
                visited_smalls[start.name] = 2
        elif start.name == 'start':
            visited_smalls[start.name] = 2

        if not self.checkhas2(curr_path):
            for n in start.neighbors:
                if n.name not in visited_smalls or visited_smalls[n.name] == 1:
                    self.findpath2(n, complete_path, visited_smalls, small2,curr_path)

        if start.name in visited_smalls:
            if visited_smalls[start.name] == 2:
                visited_smalls[start.name] = 1
            else:
                del visited_smalls[start.name]
        curr_path.reverse()
        curr_path.remove(start.name)
        curr_path.reverse()
                
            
        return self.rawpaths

class Cave:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.neighbors = []

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

class CrabMover:
    def __init__(self, days=80):
        self.crab_file = 'crabs.txt'
        self.crabs = []
        
    def getcrabs(self):
        with open(self.crab_file) as f:
            lines = f.readlines() # list containing lines of file

            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                crabs = line.split(',')
                self.crabs = [int(i) for i in crabs]

    def getminfuel(self):
        self.getcrabs()

        maxc = max(self.crabs)
        minc = min(self.crabs)
        sums=[]
        for i in range(minc,maxc+1):
            currsums = 0
            for c in self.crabs:
                fueluse = abs(c-i)
                currsums =currsums + fueluse
            sums.append(currsums)
        return min(sums)

    def getminfuel2(self):
        self.getcrabs()

        maxc = max(self.crabs)
        minc = min(self.crabs)
        sums=[]
        for i in range(minc,maxc+1):
            currsums = 0
            for c in self.crabs:
                fueluse = self.getsteps(abs(c-i)+1)
                currsums =currsums + fueluse
            sums.append(currsums)
        return min(sums)

    def getsteps(self, diff):
        return ((diff ** 2) - diff) / 2
    

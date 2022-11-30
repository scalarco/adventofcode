class FishSim:
    def __init__(self, days=80):
        self.fish_file = 'fish.txt'
        self.fish = []
        self.days = days
        
    def getfish(self):
        with open(self.fish_file) as f:
            lines = f.readlines() # list containing lines of file

            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                fish = line.split(',')
                self.fish = [int(i) for i in fish]

    def simulateFish(self):
        self.getfish()

        for day in range(0, self.days):
            new_fish = []
            for f in range(0, len(self.fish)):
                if self.fish[f] > 0:
                    self.fish[f] = self.fish[f] - 1
                else:
                    self.fish[f] = 6
                    new_fish = new_fish + [8]
            self.fish = self.fish + new_fish
        return len(self.fish)

    def simulateFish2(self):
        self.getfish()

        fishdict = {'0': 0, '1': 0, '2': 0, '3':0, '4': 0, '5': 0, '6':0, '7': 0, '8': 0}
        for f in self.fish:
            fishdict[str(f)] = fishdict[str(f)] + 1

        for day in range(0, self.days):
            r=8
            prev_val = 0
            while r>=0:
                curr_val = fishdict[str(r)]
                fishdict[str(r)] = prev_val
                prev_val = curr_val

                if r == 0:
                    fishdict['8'] = prev_val
                    fishdict['6'] = fishdict['6'] + prev_val
                r = r-1

        return sum(fishdict.values())

class OctopusSim:
    def __init__(self):
        self.flash_file = 'flashes.txt'
        self.octopus_map = []
        self.total_rows = 0
        self.total_columns = 0
        
        
    def getOctopus(self):
        with open(self.flash_file) as f:
            self.octopus_map = [list(line.strip()) for line in f]
            self.total_rows = len(self.octopus_map)
            self.total_columns = len(self.octopus_map[0])
            for r in range(0, self.total_rows):
                for c in range(0,self.total_columns):
                    self.octopus_map[r][c] = int(self.octopus_map[r][c]) #turn 2D array into ints

    def getFlashes(self):
        self.getOctopus()
        total_flashes = 0
        
        for s in range(0,100): #100 steps
            for r in range(0, self.total_rows): 
                for c in range(0, self.total_columns):
                    self.octopus_map[r][c] = self.octopus_map[r][c] + 1 #first increment all values

            flashed = [[0 for i in range(0,10)] for j in range(0,10)] #reset flashed map
            for r in range(0, self.total_rows):
                for c in range(0, self.total_columns): 
                    if self.octopus_map[r][c] > 9:
                        flashes_step = self.flash(r, c, flashed, 0)
                        total_flashes = total_flashes + flashes_step

            for r in range(0, self.total_rows):
                for c in range(0, self.total_columns): 
                    if self.octopus_map[r][c] > 9:
                        self.octopus_map[r][c] = 0 #reset to 0 flashed octopi

        return total_flashes

    def getSyncFlash(self):
        self.getOctopus()        
        
        for s in range(0,100000): #sufficiently large number of steps
            for r in range(0, self.total_rows): 
                for c in range(0, self.total_columns):
                    self.octopus_map[r][c] = self.octopus_map[r][c] + 1 #first increment all values

            flashed = [[0 for i in range(0,10)] for j in range(0,10)] #reset flashed map
            for r in range(0, self.total_rows):
                for c in range(0, self.total_columns): 
                    if self.octopus_map[r][c] > 9:
                        flashes_step = self.flash(r, c, flashed, 0)

            if not any(0 in x for x in flashed): #if all octopus flashed return step
                return s + 1 #It needs to be "after" the step has happened for whatever reason
            
            for r in range(0, self.total_rows):
                for c in range(0, self.total_columns): 
                    if self.octopus_map[r][c] > 9:
                        self.octopus_map[r][c] = 0 #reset to 0 flashed octopi

        return None
    
    def flash(self, r, c, flashed_map, flash_count):
        if r not in range(0, self.total_rows) or c not in range(0, self.total_columns): #index out of range
            return flash_count
        
        
        if flashed_map[r][c]: #already flashed so do nothing
            return flash_count
        
        self.octopus_map[r][c] = self.octopus_map[r][c] + 1 #charge the octopus
        if self.octopus_map[r][c] > 9: #This octopus flashed
            flashed_map[r][c] = 1
            flash_count = flash_count + 1
        else:
            return flash_count

        #Try to flash all the neighbors
        flash_count = self.flash(r-1, c, flashed_map, flash_count)
        flash_count = self.flash(r-1, c-1, flashed_map, flash_count)
        flash_count = self.flash(r-1, c+1, flashed_map, flash_count)
        flash_count = self.flash(r, c-1, flashed_map, flash_count)
        flash_count = self.flash(r, c+1, flashed_map, flash_count)
        flash_count = self.flash(r+1, c, flashed_map, flash_count)
        flash_count = self.flash(r+1, c-1, flashed_map, flash_count)
        flash_count = self.flash(r+1, c+1, flashed_map, flash_count)

        return flash_count
                

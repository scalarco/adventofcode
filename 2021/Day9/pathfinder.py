class PathFinder:
    def __init__(self):
        self.heatmap_file = 'heatmap.txt'
        self.heatmap = []

    def getHeatmap(self):
        with open(self.heatmap_file) as f:
            self.heatmap = [list(line.strip()) for line in f]

    def getLowest(self):
        self.getHeatmap()
        risk_sum = 0
        total_rows = len(self.heatmap)
        total_columns = len(self.heatmap[0])

        for r in range(0, total_rows):
            for c in range(0, total_columns):
                neighbors = []

		if r>0:
			neighbors.append(int(self.heatmap[r-1][c]))
		if r< (total_rows - 1):
			neighbors.append(int(self.heatmap[r+1][c]))
		if c > 0:
			neighbors.append(int(self.heatmap[r][c-1]))
		if c < (total_columns - 1):
			neighbors.append(int(self.heatmap[r][c+1]))
		if int(self.heatmap[r][c]) < min(neighbors):
			risk_sum = risk_sum + int(self.heatmap[r][c]) + 1

    def getBasins(self):
        self.getHeatmap()

        total_rows = len(self.heatmap)
        total_columns = len(self.heatmap[0])
        visited = [[0 for i in range(0,100)] for j in range(0,100)]
        basins = []
        
        for r in range(0, total_rows):
            for c in range(0, total_columns):
                curr_bas = self.search(visited, r, c, 0)
                basins.append(curr_bas)
        b = sorted(basins)
        b.reverse()
        return (b[0] * b[1] * b[2])

    def search(self, visitedmap, r, c, basin_size):
        if visitedmap[r][c]:
            return basin_size
        
        visitedmap[r][c] = 1
        if int(self.heatmap[r][c]) == 9:
            return basin_size

        basin_size = basin_size + 1
        if r>0:
            basin_size = self.search(visitedmap, r-1, c, basin_size) 
        if r< (len(self.heatmap) - 1):
            basin_size = self.search(visitedmap, r+1, c, basin_size) 
        if c > 0:
            basin_size = self.search(visitedmap, r, c-1, basin_size) 
        if c < (len(self.heatmap[0]) - 1):
            basin_size = self.search(visitedmap, r, c+1, basin_size) 

        return basin_size

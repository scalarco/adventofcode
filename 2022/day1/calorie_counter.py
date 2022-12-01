class CalorieCounter:
    def __init__(self):
        self.calorie_file = 'calories.txt'
        self.elf_list = []
        
    def getcalories(self):
        with open(self.calorie_file) as f:
            lines = f.readlines() # list containing lines of file
            curr_elf_calories = 0
            curr_elf = 1
            max_elf = 0
            max_elf_calories = 0
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if line:
                    curr_elf_calories = curr_elf_calories + int(line)
                else:
                    if curr_elf_calories > max_elf_calories:
                        max_elf = curr_elf
                        max_elf_calories = curr_elf_calories
                    curr_elf = curr_elf + 1
                    curr_elf_calories = 0
            return max_elf_calories

    def getcalorieslist(self):
        with open(self.calorie_file) as f:
            lines = f.readlines() # list containing lines of file
            curr_elf_calories = 0
            curr_elf = 1
            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                if line:
                    curr_elf_calories = curr_elf_calories + int(line)
                else:
                    self.elf_list = self.elf_list + [curr_elf_calories]
                    curr_elf = curr_elf + 1
                    curr_elf_calories = 0
            return self.elf_list

    def getsumthree(self):
        self.elf_list.sort()
        self.elf_list.reverse()
        return self.elf_list[0] + self.elf_list[1] + self.elf_list[2]
    

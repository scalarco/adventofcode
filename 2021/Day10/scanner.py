class SyntaxScanner:
    def __init__(self):
        self.syntax_file = 'syntax.txt'
        self.point_lookup1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.point_lookup2 = {')': 1, ']': 2, '}': 3, '>': 4}
        self.syntax_lines = []
        self.map_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
        self.open_chars = ['(','[','{','<']
        self.close_chars = [')',']','}','>']
        
    def getsyntax(self):
        with open(self.syntax_file) as f:
            lines = f.readlines() # list containing lines of file

            for line in lines:
                line = line.strip() # remove leading/trailing white spaces
                self.syntax_lines.append(line)

    def getErrors(self):
        self.getsyntax()
        sum_val = 0
        for l in self.syntax_lines:
            corrupted_char = self.findBadChar(l)
            if corrupted_char:
                sum_val = sum_val + self.point_lookup1[corrupted_char]
        return sum_val

    def getIncomplete(self):
        self.getsyntax()
        completion_strings = []
        points = []
        
        for l in self.syntax_lines:
            corrupted_char = self.findBadChar(l)
            if not corrupted_char:
                completion_strings.append(self.findClosing(l))

        for s in completion_strings:
            points.append(self.scoreLine(s))

        val = int(len(points)/2)
        return sorted(points)[val]

    def findBadChar(self, line):
        expecting = []
        for c in line:
            if c in self.open_chars:
                expecting = [self.map_dict[c]] + expecting
            else:
                if c != expecting[0]:
                    return c
                else:
                    expecting.remove(c)
        return None

    def findClosing(self, line):
        expecting = []
        for c in line:
            if c in self.open_chars:
                expecting = [self.map_dict[c]] + expecting
            else:
                expecting.remove(c)
        return expecting

    def scoreLine(self, line):
        total = 0
        for c in line:
            total = total * 5
            total = total + self.point_lookup2[c]
        return total

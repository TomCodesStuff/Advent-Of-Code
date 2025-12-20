import math
import re
from solution_base.solution import Solution 


class DayTwo(Solution): 

    def parse(self, line):
        return re.sub("Game|[,;:]", "", line.strip("\n")).lstrip().split(" ")


    def task_one(self):        
        total = 0
        gamePossible = True
        colorDict = {
            "red" : 12,
            "green": 13,
            "blue": 14
        }

        for line in self.get_puzzle_input():
            line = self.parse(line)
            for i in range(2, len(line), 2): 
                if(int(line[i - 1]) > colorDict[line[i]]): 
                    gamePossible = False
                    break
                else: gamePossible = True
            if(gamePossible): total += int(line[0])
            gamePossible = True
        return total
        

    def task_two(self):
        total = 0
        colorDict = {
            "red" : 0,
            "green": 0,
            "blue": 0
        }

        for line in self.get_puzzle_input():
            line = self.parse(line)
            for i in range(2, len(line), 2): 
                if(int(line[i - 1]) > colorDict[line[i]]):
                    colorDict[line[i]] = int(line[i - 1])
            total += math.prod(list(colorDict.values()))
            colorDict = dict.fromkeys(colorDict, 0) 
        return total


if __name__ == "__main__": 
    s = DayTwo() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")

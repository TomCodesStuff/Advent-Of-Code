import re 
import math
from solution_base import Solution 


class DaySix(Solution): 


    def parse_task_one(self, line): 
        return re.findall("[0-9]*[0-9]", line)


    # Speed = distance / time 
    def task_one(self):
        total = 1
        puzzle_input = self.get_puzzle_input()
        times = self.parse_task_one(puzzle_input[0])
        distance = self.parse_task_one(puzzle_input[1]) 
        for index, time in enumerate(times):
            waysToFinish = 0
            for i in range(1, int(time)):
                if(((int(time) - i) * i) > int(distance[index])): waysToFinish += 1
            if(waysToFinish > 0): total *= waysToFinish
        return total


    def parse_task_two(self, line):
        return int(''.join(re.findall("[0-9]", line)))


    def task_two(self):
        puzzle_input = self.get_puzzle_input()
        time = self.parse_task_two(puzzle_input[0])  
        distance = self.parse_task_two(puzzle_input[1])
        waysToFinish = 0
        for i in range(1, time):
            if(((time - i) * i) > distance): waysToFinish += 1
        return waysToFinish


    # Optimum solution by calculating the discriminant. 
    def optimal_task_two(self):
        puzzle_input = self.get_puzzle_input()
        time = self.parse_task_two(puzzle_input[0])  
        distance = self.parse_task_two(puzzle_input[1])
        return int(math.sqrt(time ** 2 - (4 * distance)))



if __name__ == "__main__": 
    s = DaySix() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
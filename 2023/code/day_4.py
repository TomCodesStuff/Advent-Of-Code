import re
from solution_base.solution import Solution 


class DayFour(Solution): 

    def parse(self, line):
        nums =  re.sub("^Card [0-9]: ", "", line).rstrip().split("|")
        for i in range (len(nums)):
            nums[i] = re.sub("^[ ]+|[ ]+$", "", nums[i]).split(" ") 
            nums[i] = (set([i for i in nums[i] if i != ""]))
        return nums


    def task_one(self):
        total = 0
        for line in self.get_puzzle_input():
            numbers = self.parse(line)
            matches = len(numbers[0].intersection(numbers[1]))
            if(matches): total += 2 ** (matches - 1) 
        return total


    def task_two(self):
        total = 0
        matches = {}
        scratchCards = {}
        
        for index, line in enumerate(self.get_puzzle_input()):
            numbers = self.parse(line)
            matches[index] = len(numbers[0].intersection(numbers[1]))
            scratchCards[index] = 1
        
        for key, value in matches.items():
            for i in range(1, value + 1):
                scratchCards[key + i] += scratchCards[key]
            total += scratchCards[key]
        return total    


if __name__ == "__main__": 
    s = DayFour() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
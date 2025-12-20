import re
from solution_base.solution import Solution 


class DayOne(Solution): 


    def merge_digits(self, nums):
        if(len(nums) > 1):
            return int(nums[0] + nums[-1])
        else:
            return int(nums[0] + nums[0])


    def task_one(self): 
        total = 0
        for line in self.get_puzzle_input():
                total += self.merge_digits(re.findall("[0-9]", line))
        return total 


    def task_two(self):
        digits = {
            "one": "one1one", 
            "two": "two2two", 
            "three": "three3three", 
            "four": "four4four", 
            "five": "five5five", 
            "six": "six6six", 
            "seven": "seven7seven", 
            "eight": "eight8eight", 
            "nine": "nine9nine", 
            "zero": "zero0zero"
        }

        total = 0
        for line in self.get_puzzle_input():
            for digit, numeric in digits.items():
                line = line.replace(digit, numeric)
            total += self.merge_digits(re.findall("[0-9]", line))
        return total 
    

if __name__ == "__main__": 
    s = DayOne() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
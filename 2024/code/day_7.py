import re 
from solution_base import Solution 


class DaySeven(Solution):


    def parse_input(self):  
        target_values = []
        for line in self.get_puzzle_input():
            nums = list(map(int, re.findall("[0-9]+", line)))
            target_values.append((nums[0], nums[1:])) 
        return target_values


    def is_solvable_one(self, target, curr_val, arr):
        if arr == []:
            if target == curr_val: return 1
            return 0

        return 1 if self.is_solvable_one(target, curr_val * arr[0], arr[1:])\
            else self.is_solvable_one(target, curr_val + arr[0], arr[1:])

        
    def task_one(self):
        target_values = self.parse_input() 
        calibration_result = 0
        for target, values in target_values: 
            if(self.is_solvable_one(target, values[0], values[1:])): 
                calibration_result += target
        return calibration_result


    def is_solvable_two(self, target, current, arr):
        if arr == []:
            if current == target: return 1
            return 0
    
        if(self.is_solvable_two(target, current + arr[0], arr[1:])): return 1
        if(self.is_solvable_two(target, current * arr[0], arr[1:])): return 1
        return self.is_solvable_two(target,  int(str(current) + str(arr[0])), arr[1:])

        
    def task_two(self): 
        target_values = self.parse_input() 
        calibration_result = 0
        for target, values in target_values: 
            if self.is_solvable_two(target, values[0], values[1:]): 
                calibration_result += target  
        return calibration_result 


if __name__ == "__main__": 
    s = DaySeven() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
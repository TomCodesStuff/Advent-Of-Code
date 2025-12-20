from functools import cache
from solution_base import Solution 


class DayEleven(Solution):


    def parse_input(self):  
        return list(map(int, self.get_puzzle_input()[0].split(" ")))


    @cache
    def check_stones(self, val, it_count):
        if it_count == 0:
            return 1
        
        if val == 0: 
            return self.check_stones(1, it_count - 1)

        rock_str = str(val)
        num_digits = len(rock_str)

        if(num_digits % 2 == 0):
            half = num_digits // 2 
            return self.check_stones(int(rock_str[:half]), it_count - 1) + \
                self.check_stones(int(rock_str[half:]), it_count - 1)  
        else: return self.check_stones(val * 2024, it_count - 1)


    def task_one(self): 
        c = 0
        for stone in self.parse_input() : 
            c += self.check_stones(stone, 25) 
        return c


    def task_two(self):  
        c= 0
        for stone in self.parse_input() : 
            c += self.check_stones(stone, 75)
        return c


if __name__ == "__main__": 
    s = DayEleven() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
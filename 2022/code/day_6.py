from solution_base import Solution 


class DaySix(Solution): 


    # Checks if character appears more then once in a string 
    def unique_char(self, seq):
        for char in seq:
            if(seq.count(char) > 1): return False
        return True 


    # Solution 1
    def task_one(self):
        for line in self.get_puzzle_input():
            for i in range(len(line)):
                if(self.unique_char(line[i:i + 4]) == False): continue 
                else: return i + 4


    # Solution 2
    def task_two(self):
        for line in self.get_puzzle_input():
            for i in range(len(line)):
                if(self.unique_char(line[i:i + 14]) == False): continue 
                else: return i + 14


if __name__ == "__main__": 
    s = DaySix() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
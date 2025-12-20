import re
from solution_base import Solution 


class DayThree(Solution):


    def parse_input(self, is_task_two : bool):  
        instructions = [] 
        # Regex for part one
        exp = "mul\\([0-9]+,[0-9]+\\)"
        if(is_task_two): 
            # Regex for part two
            exp += "|don't\\(\\)|do\\(\\)"
        
        # Find occurences of regex in each line 
        for line in self.get_puzzle_input(): 
            instructions.append(re.findall(exp, line.strip())) 
        # Flatten 2D array into 1D and return
        return [j for i in instructions for j in i]
        

    def task_one(self): 
        # Valid mul instructions
        valid_instructions = self.parse_input(is_task_two=False)
        total = 0
        for instruction in valid_instructions: 
            # Extract numbers
            x, y = re.findall("[0-9]*,[0-9]*", instruction)[0].split(",") 
            total += int(x) * int(y)
        return total


    def task_two(self):
        # Valid mul, do, don't instructions
        valid_instructions = self.parse_input(is_task_two=True)
        ignore = False  
        total = 0 
        for instruction in valid_instructions: 
            # Split into instructions and param e.g "mul", "1, 2)"
            instruction, param = instruction.split("(")
            if(instruction == "do"): ignore = False
            if(instruction == "don't"): ignore = True 
            elif(instruction == "mul" and not ignore):
                # Extract Numbers
                x, y = re.findall("[0-9]*,[0-9]*", param)[0].split(",")
                total += int(x) * int(y) 
        return total


if __name__ == "__main__": 
    s = DayThree() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
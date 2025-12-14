from solution_base.solution import Solution 


class DayOne(Solution):


    def task_one(self) -> int: 
        dial_num = 50 
        psswd = 0
        for line in self.get_puzzle_input(): 
            direction, rotation = line[0], int(line[1:])           
            if direction == "L":  
                dial_num = (dial_num - rotation) % 100
            elif direction == "R": 
                dial_num = (dial_num + rotation) % 100 
            if dial_num == 0: psswd += 1 
        return psswd 


    def task_two(self) -> int:
        dial_num = 50 
        psswd = 0

        for line in self.get_puzzle_input(): 
            direction, rotation = line[0], int(line[1:])   
            prev_dial_num = dial_num
            if direction == "L":  
                pos = dial_num - rotation
                dial_num = (dial_num - rotation) % 100
            elif direction == "R": 
                pos = dial_num + rotation
                dial_num = (dial_num + rotation) % 100  
            if pos < 0: 
                if prev_dial_num == 0:
                    psswd += (pos // -100)  
                else: psswd += (pos // -100) + 1
            elif pos > 99: 
                psswd += (pos // 100) 
            elif pos == 0: psswd += 1 
        return psswd 


if __name__ == "__main__": 
    s = DayOne() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
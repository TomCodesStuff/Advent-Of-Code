from solution_base.solution import Solution 


class DayTwo(Solution):


    def parse_puzzle_input(self):
        puzzle_input = self.get_puzzle_input() 
        return [xs.split("-") for x in puzzle_input for xs in x.split(",")]


    def is_num_invalid(self, num : str) -> bool:
        if len(num) % 2: return False  
        mid_point = len(num) // 2 
        if num[:mid_point] == num[mid_point:]: return True
        else: return False
        

    def task_one(self) -> int:   
        previous_invalid = set()
        total = 0
        for range_start, range_end in self.parse_puzzle_input(): 
            for num in range(int(range_start), int(range_end) + 1):   
                if num in previous_invalid: total += num
                if(self.is_num_invalid(str(num))): 
                    total += num 
                    previous_invalid.add(num)
        return total  


    def is_num_valid(self, num : str) -> bool: 
        sequence, next_char_idx = num[0], 1
        is_valid = True
        while(next_char_idx <= len(num) // 2 and is_valid):  
            next_seq = False
            if len(num) % len(sequence): next_seq = True
            else:
                for i in range(len(sequence), len(num), len(sequence)):  
                    if num[i:i + len(sequence)] != sequence: 
                        next_seq = True
                        break
            if next_seq: 
                sequence += num[next_char_idx] 
                next_char_idx += 1 
            else: 
                is_valid = False 
        return is_valid


    def task_two(self) -> int:
        previous_invalid = set()
        total = 0 
        for range_start, range_end in self.parse_puzzle_input(): 
            for num in range(int(range_start), int(range_end) + 1):   
                if num in previous_invalid: total += num
                elif not self.is_num_valid(str(num)):
                    total += num  
                    previous_invalid.add(num)
        return total


if __name__ == "__main__": 
    s = DayTwo() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
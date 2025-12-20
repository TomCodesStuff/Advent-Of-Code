from solution_base import Solution 


class DayThree(Solution):


    def __init__(self) -> None:
        self.joltage_len = 12 


    def task_one(self) -> int:
        total = 0
        for battery_bank in self.get_puzzle_input():   
            cell_one, cell_two = "0", "0"
            for i in range(len(battery_bank) - 1):
                if battery_bank[i] > cell_one: 
                    cell_one = battery_bank[i]
                    cell_two = battery_bank[i + 1]
                else: 
                    cell_two = max(cell_two, battery_bank[i + 1])
            total += int(cell_one + cell_two)
        return total


    def task_two(self) -> int: 
        total = 0 
        for battery_bank in self.get_puzzle_input(): 
            joltage_cells = ["0" for _ in range(self.joltage_len)] 
            cell_idx, limit_idx = 0, len(battery_bank) - self.joltage_len

            i = 0
            while(cell_idx < len(joltage_cells)):           
                highest_val, next_idx = "0", 0 
                for j in range(i, limit_idx + 1): 
                    if battery_bank[j] > highest_val: 
                        highest_val = battery_bank[j] 
                        next_idx = j + 1
                joltage_cells[cell_idx] = highest_val 
                cell_idx += 1 
                i = next_idx
                limit_idx = len(battery_bank) - self.joltage_len + cell_idx
            total += int("".join(joltage_cells))
        return total


if __name__ == "__main__": 
    s = DayThree() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
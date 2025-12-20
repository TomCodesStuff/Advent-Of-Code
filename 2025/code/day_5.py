from solution_base import Solution  


class DayFive(Solution):


    def parse_puzzle_input(self): 
        number_ranges = [] 
        ids_to_check = [] 
 
        for line in self.get_puzzle_input():
            if "-" in line: number_ranges.append([int(x) for x in line.split("-")])
            elif line != "": ids_to_check.append(int(line))
        return (number_ranges, ids_to_check)


    def task_one(self) -> int:  
        total = 0
        number_ranges, ids_to_check = self.parse_puzzle_input() 
        for id in ids_to_check: 
            for start, end in number_ranges: 
                if start  <= id <= end: 
                    total += 1
                    break 
        return total


    def task_two(self) -> int: 
        total = 0
        number_ranges, _ = self.parse_puzzle_input() 
        number_ranges.sort()   
        i = 0 
        while(i < len(number_ranges) - 1): 
            _, range_end = number_ranges[i]
            next_range_start, _ = number_ranges[i + 1] 
            if range_end >= next_range_start: 
                number_ranges[i][1] = max(number_ranges[i][1], number_ranges[i + 1][1])
                number_ranges.pop(i + 1)
            else: i += 1
        for start, end in number_ranges:  
            total += (end - start + 1)
        return total


if __name__ == "__main__": 
    s = DayFive() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
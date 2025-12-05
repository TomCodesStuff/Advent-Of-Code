if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath  






def get_puzzle_input(): 
    number_ranges = [] 
    ids_to_check = []
    with open(getFilePath()) as f:  
        while(line := f.readline()): 
            line = line.strip()
            if "-" in line: number_ranges.append([int(x) for x in line.split("-")])
            elif line != "": ids_to_check.append(int(line))
    return (number_ranges, ids_to_check)



def task_one() -> int:  
    total = 0
    number_ranges, ids_to_check = get_puzzle_input() 
    for id in ids_to_check: 
        for start, end in number_ranges: 
            if start  <= id <= end: 
                total += 1
                break 
    return total


def task_two() -> int: 
    total = 0
    number_ranges, _ = get_puzzle_input() 
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


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")
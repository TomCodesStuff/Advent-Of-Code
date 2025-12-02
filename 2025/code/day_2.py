if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def get_puzzle_input():
    with open(getFilePath()) as f:  
        return [x.split("-") for x in f.readline().split(",")]


def is_num_invalid(num : str) -> bool:
    if len(num) % 2: return False  
    mid_point = len(num) // 2 
    if num[:mid_point] == num[mid_point:]: return True
    else: return False
    

def task_one() -> int:   
    previous_invalid = set()
    total = 0
    for range_start, range_end in get_puzzle_input(): 
        for num in range(int(range_start), int(range_end) + 1):   
            if num in previous_invalid: total += num
            if(is_num_invalid(str(num))): 
                total += num 
                previous_invalid.add(num)
    return total  


def is_num_valid(num : str) -> bool: 
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


def task_two() -> int:
    previous_invalid = set()
    total = 0 
    for range_start, range_end in get_puzzle_input(): 
        for num in range(int(range_start), int(range_end) + 1):   
            if num in previous_invalid: total += num
            elif not is_num_valid(str(num)):
                total += num  
                previous_invalid.add(num)
    return total


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")
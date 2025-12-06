if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath  


def get_puzzle_input(): 
    homework_problems = []
    with open(getFilePath()) as f:
        while(line := f.readline()):  
            homework_problems.append(line.strip().split())
    # Transpose matrix so problems are by row not by column 
    return [[row[i] for row in homework_problems] for i in range(len(homework_problems[0]))]


def multiply(nums) -> int:  
    res = 1
    for num in nums: 
        res *= int(num)  
    return res


def add(nums) -> int:  
    res = 0
    for num in nums: 
        res += int(num) 
    return res


def task_one() -> int: 
    total = 0
    homework_problems = get_puzzle_input() 
    for problem in homework_problems:  
        if problem[-1] == "*": total += multiply(problem[:-1])
        elif problem[-1] == "+": total += add(problem[:-1])
    print(total)


def task_two() -> int:
    print(get_puzzle_input()) 
    return




task_one()
task_two()
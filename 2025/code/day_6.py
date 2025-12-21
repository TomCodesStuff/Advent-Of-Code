from solution_base import Solution  


class DaySix(Solution): 


    def parse_puzzle_input(self): 
        spaces_sets = []
        common_spaces = set()
        homework_problems = []
        for line in self.get_puzzle_input(): 
            homework_problems.append(line)
            spaces_sets.append(set([i for i in range(len(line)) if line[i] == " "]))
        
        common_spaces = spaces_sets[0]
        for space_set in spaces_sets[1:]: 
            common_spaces = common_spaces.intersection(space_set)
        common_spaces = sorted(list(common_spaces))
        common_spaces = [(i + 1, j) for (i, j) in zip([-1] + common_spaces, common_spaces + [None])]
        homework_problems = [[problem[i:j] for (i, j) in common_spaces] for problem in homework_problems]
        return [[row[i] for row in homework_problems] for i in range(len(homework_problems[0]))]


    def multiply(self, nums) -> int:  
        res = 1
        for num in nums: res *= int(num)  
        return res


    def add(self, nums) -> int:  
        res = 0
        for num in nums: res += int(num) 
        return res


    def task_one(self) -> int: 
        total = 0
        for problem in self.parse_puzzle_input():  
            operator = problem[-1].strip()
            if operator == "*": total += self.multiply(problem[:-1])
            elif operator == "+": total += self.add(problem[:-1])
        return total


    def task_two(self) -> int: 
        total = 0
        for problem in self.parse_puzzle_input():  
            nums = [[row[i] for row in problem[:-1]] for i in range(len(problem[0]))] 
            nums = ["".join(split_num) for split_num in nums]
            operator = problem[-1].strip()
            if operator == "+": total += self.add(nums)
            elif operator == "*": total += self.multiply(nums)
        return total


if __name__ == "__main__": 
    s = DaySix() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
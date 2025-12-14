from solution_base.solution import Solution 


class DayOne(Solution):


    # Processes the input as needed for each task
    def parse_puzzle_input(self):
        left_list = [] 
        right_list = [] 

        for line in self.get_puzzle_input():
            nums = line.strip().split("  ")
            left_list.append(int(nums[0]))
            right_list.append(int(nums[1])) 
        return left_list, right_list


    def task_one(self): 
        left_list, right_list = self.parse_puzzle_input() 
        
        # Sort both lists
        left_list.sort()
        right_list.sort() 
        total = 0
        
        for left_num, right_num in zip(left_list, right_list): 
            # Get difference for each pair, add to total
            total += abs(left_num - right_num)
        return total


    def task_two(self):
        left_list, right_list = self.parse_puzzle_input()    
        # Map left list numbers to occurences in right list
        num_to_occur = {val : 0 for val in left_list} 
        # Get occurence of each number in rigt list
        for num in right_list:
            if num in num_to_occur: 
                num_to_occur[num] += 1
        
        total = 0
        for num in left_list:  
            # Add number * occurences in right list
            total += num * num_to_occur[num]    
        return total


if __name__ == "__main__": 
    s = DayOne() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
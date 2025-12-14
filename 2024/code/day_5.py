from solution_base.solution import Solution 


class DayFive(Solution):


    def parse_input(self): 
        num_to_nums_before = {} 
        puzzle_input = self.get_puzzle_input()
        sep_idx = puzzle_input.index("")
        for line in puzzle_input[:sep_idx]:
            if line == "": break
            x, y = line.split("|")
            if(y in num_to_nums_before): 
                num_to_nums_before[y].add(x)
            else: num_to_nums_before[y] = set([x])
        
        return ([line.split(",")[::-1] for line in puzzle_input[sep_idx + 1:]], num_to_nums_before)


    def categorise_updates(self, updates, nums_order, update_flag): 
        invalid_updates = []
        for update in updates: 
            num_set = set()
            for num in update: 
                if(len(num_set.intersection(nums_order.get(num, set())))): 
                    invalid_updates.append(update)
                    break
                num_set.add(num) 
        if(update_flag):
            return [i for i in updates if i not in invalid_updates]
        return invalid_updates


    def task_one(self):
        updates, nums_order = self.parse_input()  
        update_sum = 0
        valid_updates = self.categorise_updates(updates, nums_order, True) 
        for update in valid_updates:
            update_sum += int(update[len(update) // 2])
        return update_sum


    def task_two(self): 
        updates, nums_order = self.parse_input()  
        update_sum = 0
        invalid_updates = self.categorise_updates(updates, nums_order, False)  
        for update in invalid_updates: 
            num_set = set() 
            fixed_update = []
            for num in update:
                conflicts = num_set.intersection(nums_order.get(num, set()))
                if(len(conflicts) == 0): 
                    fixed_update.append(num) 
                else:
                    idx = float("inf")
                    for conflict in conflicts:
                        idx = min(fixed_update.index(conflict), idx)      
                    fixed_update.insert(idx, num)
                num_set.add(num) 
            update_sum += int(fixed_update[len(fixed_update) // 2])
        return update_sum

            
if __name__ == "__main__": 
    s = DayFive() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
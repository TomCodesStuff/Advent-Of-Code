from solution_base.solution import Solution 


class DayNine(Solution): 


    def next_reading(self, history: list):
        if(all(x == 0 for x in history)): return 0
        else: return history[-1] + self.next_reading([history[i + 1] - history[i] for i in range(len(history) - 1)]) 


    def previous_reading(self, history: list):
        if(all(x == 0 for x in history)): return 0
        else: return history[0] - self.previous_reading([history[i + 1] - history[i] for i in range(len(history) - 1)]) 


    def task_one(self):
        readings = [list(map(int, line.split(" "))) for line in self.get_puzzle_input()]
        total = 0
        for history in readings:  
            total += self.next_reading(history)    
        return total


    def task_two(self):
        readings = [list(map(int, line.split(" "))) for line in self.get_puzzle_input()]
        total = 0
        for history in readings:  
            total += self.previous_reading(history)    
        return total


if __name__ == "__main__": 
    s = DayNine() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
from solution_base import Solution 


class DayOne(Solution): 

    # Solution to part 1
    def task_one(self):
        highestCals = 0 
        totalCals = 0
        
        for line in self.get_puzzle_input():           
            if(not line == ""): totalCals += int(line)    
            else:
                if(totalCals > highestCals):
                    highestCals = totalCals
                totalCals = 0
        return highestCals


    # Solution to part 2
    def task_two(self):
        totalCals = 0 
        highest, second, third = 0, 0, 0 
        
        for line in self.get_puzzle_input():   
            if(line != ""): totalCals += int(line) 
            else:
                # Adjusts top 3 highest calories
                if(highest == 0):
                    highest = totalCals
                elif(totalCals > highest):
                    third = second 
                    second = highest 
                    highest = totalCals
                elif(totalCals > second):
                    third = second
                    second = totalCals 
                elif(totalCals > third):
                    third = totalCals 
                totalCals = 0 
        return (highest + second + third)


if __name__ == "__main__": 
    s = DayOne() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
from solution_base import Solution 


class DayTen(Solution): 
    def __init__(self):
        self.checkCycle = 20
        self.crtWidth = 40


    # Solution 1
    def task_one(self):
        cycle, x, total = 1, 1, 0 

        for line in self.get_puzzle_input(): 
                line = line.split(" ")  
                if(line[0] == "addx"):
                    cycle += 1 
                    if(cycle == self.checkCycle or ((cycle / self.checkCycle) % 2 == 1 and (cycle / self.checkCycle) <= 11)): 
                        total += (x * cycle)
                    x += int(line[1])
                    cycle += 1
                else: cycle += 1
                if(cycle == self.checkCycle or ((cycle / self.checkCycle) % 2 == 1 and (cycle / self.checkCycle) <= 11)): total += (x * cycle)
        return total    


    # Solution two
    def task_two(self): 
        cycle, x = 1, 1
        screen = ["." for _ in range(self.crtWidth)]
        crtMessage = []


        for line in self.get_puzzle_input(): 
                line = line.split(" ")
                if(abs(x - (cycle - 1)) <= 1): screen[(cycle) - 1] = "#"
                if(line[0] == "addx"):
                    cycle += 1  
                    if(abs(x - (cycle-1)) <= 1): screen[(cycle) - 1] = "#"
                    if(cycle == self.crtWidth): 
                        crtMessage.append(screen)
                        screen = ["." for _ in screen]
                        cycle = 0
                    x += int(line[1])
                    cycle+=1
                else: cycle+=1
                
                if(cycle == self.crtWidth):
                    crtMessage.append(screen)
                    screen = ["." for _ in screen]
                    cycle = 0
        return crtMessage


if __name__ == "__main__": 
    s = DayTen() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: (See Below):")
    for row in s.task_two(): 
        print("".join(row))
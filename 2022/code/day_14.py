# This one doesn't run as slow as other days, that's good I guess
from solution_base import Solution 


class DayFourteen(Solution): 

    # Solution 1
    def task_one(self):
        rocks = set()
        sand = set()
        abyss = 0
        lowest = 0

        for line in self.get_puzzle_input()[:-1]:
            line = line.split("->")
            
            for x in range(len(line) - 1):
                current = list(map(int, line[x].split(",")))
                next = list(map(int, line[x+1].split(",")))
                
                # On same x level
                if(current[0] == next[0]):
                    x = min(current[1], next[1])
                    while(x <= max(current[1], next[1])):
                        rocks.add((current[0], x))
                        x+=1 
                # Handling Y-level
                else:
                    x = min(current[0], next[0])
                    while(x <= max(current[0], next[0])):
                        rocks.add((x, current[1])) 
                        x+=1 
                if(max(current[1], next[1]) > lowest):
                    lowest = max(current[1], next[1])
        
        while not abyss:
            settled = 0
            x = 500 
            y = 0
            while not settled:
                # Handling the abyss
                if(y + 1 > lowest):
                    settled = 1
                    abyss  = 1 
                y+=1 
                
                # In sand or rocks
                if((x, y+1) in rocks or (x, y+1) in sand):
                
                    if((x-1, y+1) in rocks or (x-1, y+1) in sand):
                        # Obstructed right
                        if((x+1, y+1) in rocks or (x+1, y+1) in sand):
                            sand.add((x,y))
                            settled = 1
                        else:
                            x+=1
                        
                    else:
                        x-=1
                
        return len(sand) 

    #Solution 2
    def task_two(self):
        rocks = set()
        sand = set()
        lowest = 0
        floor = 0

        for line in self.get_puzzle_input()[:-1]:
            line = line.split("->")
            
            for x in range(len(line) - 1):
                current = list(map(int, line[x].split(",")))
                next = list(map(int,line[x + 1].split(",")))
                # On same x level
                if(current[0] == next[0]):
                    x = min(current[1], next[1])
                    while(x <= max(current[1], next[1])):
                        rocks.add((current[0], x))
                        x+=1 
                # Handling Y-level
                else:
                    x = min(current[0], next[0])
                    while(x <= max(current[0], next[0])):
                        rocks.add((x, current[1])) 
                        x+=1 
                if(max(current[1], next[1]) > lowest):
                    lowest = max(current[1], next[1]) 
                    
        lowest+=2
        while not floor:
            settled = 0
            x = 500 
            y = 0
            while not settled:
                if(y + 1 == lowest):
                    sand.add((x,y))
                    settled = 1
                    break 
                if((x,y+1) in rocks or (x, y+1) in sand):
                    if((x-1, y+1) in rocks or (x-1, y+1) in sand):
                        if((x+1,y+1) in rocks or (x+1, y+1) in sand):
                            sand.add((x,y))
                            settled = 1
                            if(x == 500 and y == 0):
                                floor = 1
                            break 
                        else:
                            x+=1
                            y+=1
                            continue
                    else:
                        x-=1
                        y+=1 
                        continue 
                y+=1
                                
        return len(sand)
      

if __name__ == "__main__": 
    s = DayFourteen() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
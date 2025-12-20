from solution_base import Solution 


class DayFive(Solution): 
    def __init__(self):
        self.value = 9 


    # Solution 1
    def task_one(self):
        stack = [[] for _ in range(self.value)]
        x = 1
        space, stackVal = 0, 0  
        i, j = 0, 0

        puzzle_input = self.get_puzzle_input()    
        line = puzzle_input[i] 
        
        while(not (line[1].isdigit())):
            while(j < len(line)):
                if(line[j] == "["):
                    stack[stackVal].append(line[j + 1])
                    stackVal+=1
                    j += 2
                    space = 0
                    continue 
                elif(line[j] == " "): 
                    space +=1
                    if(space % 4 == 0):
                        space = 0 
                        stackVal += 1 
                    j += 1
                    continue
                j += 1
            i += 1
            line = puzzle_input[i]
            
            j = 0 
            space = 0
            stackVal  = 0

        for line in puzzle_input[i + 2:]:
            data = line.strip().split(" ") 
            loop = int(data[1])
            while(x <= loop):
                popped = stack[int(data[3])-1].pop(0)
                stack[int(data[5])-1].insert(0, popped) 
                x+=1
            x = 1
        
        return "".join([i[0] for i in stack]) 


    def task_two(self):  
        stack = [[] for _ in range(self.value)]
        space, stackVal = 0, 0 
        i, j = 0, 0
        
        puzzle_input = self.get_puzzle_input()    
        line = puzzle_input[i] 
        
        while(not (line[1].isdigit())):
            while(j < len(line)):
                if(line[j] == "["):
                    stack[stackVal].append(line[j + 1])
                    stackVal += 1
                    j += 2
                    space = 0
                    continue 
                elif(line[j] == " "): 
                    space += 1
                    if(space % 4 == 0):
                        space = 0 
                        stackVal += 1 
                    j += 1
                    continue
                j += 1
            i += 1 
            line = puzzle_input[i]
            j = 0 
            space = 0
            stackVal  = 0
        
        for line in puzzle_input[i + 2:]:
            data = line.strip().split(" ") 
            loop = int(data[1])
            while(loop > 0):
                popped = stack[int(data[3])-1].pop(loop - 1)
                stack[int(data[5])-1].insert(0, popped) 
                loop-=1
        
        return "".join([i[0] for i in stack]) 


if __name__ == "__main__": 
    s = DayFive() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
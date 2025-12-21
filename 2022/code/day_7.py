from solution_base import Solution 


class DaySeven(Solution):  
    def __init__(self):
        self.dirSize = [] 
        self.diskSpace = 70000000 
        self.requireSpace = 30000000
        self.maxDirSize = 100000


    def task_one(self): 
        currentDir = [] 
        runningSize = []
        i = 0 
        total = 0 
        
        array = [] 
        for line in self.get_puzzle_input():
            data = line.split(" ")
            array.append(data) 
        
        while (i < (len(array))): 
            if(array[i][1] == "ls"):
                i+=1
                while(i < len(array) and array[i][0] != "$"):
                    if(array[i][0].isnumeric()):
                        total += int(array[i][0])  
                    i+=1  
                n = 1
                if(len(currentDir) > 1):
                    while(n < len(currentDir)):
                        runningSize[-n] = int(runningSize[-n]) + total
                        n+=1
                runningSize.append(total)
                total = 0
                continue
            elif(array[i][1] == "cd"):
                if(array[i][2] == ".."):
                    self.dirSize.append(runningSize[-1])
                    runningSize.pop()
                    currentDir.pop(0)
                else: currentDir.insert(0, array[i][2])
            i+=1    
        self.dirSize.append(runningSize.pop())
        self.dirSize.append(runningSize.pop())
        total = 0 
        for num in self.dirSize:
            if(num < self.maxDirSize): total += num
        return total


    def task_two(self):   
        # Part One needs to be completed prior to part two being run 
        if not self.dirSize: self.task_one()

        space = self.diskSpace - self.dirSize[-1]
        space = self.requireSpace - space
        self.dirSize.sort()
        i = 0 
        for i in range(len(self.dirSize)):
            if(self.dirSize[i] > space): return self.dirSize[i]


if __name__ == "__main__": 
    s = DaySeven() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
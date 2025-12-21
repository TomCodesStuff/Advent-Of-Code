from solution_base import Solution 


class Monkey:
    def __init__(self):
        self.item = [] 
        self.operationOp = 0
        self.operationNum = 0 
        self.throwTrue = 0
        self.throwFalse = 0
        self.test = 0


class DayEleven(Solution): 

    def __init__(self):
        self.numMonkeys = 8
        self.taskOneRounds = 20
        self.taskTwoRounds = 10000


    def task_one(self):
        product = 1
        monkeys = [Monkey() for _ in range(self.numMonkeys)] 
        inspected = [0 for _ in range(self.numMonkeys)]
        puzzle_input = self.get_puzzle_input()
        
        x = 0
        for line in puzzle_input[1:]:
            line = line.split()
            if len(line) == 0: continue
            if(line[0] == "Monkey"): x += 1
            elif(line[0] == "Starting"):
                for j in range(2, len(line)):
                    monkeys[x].item.append(int(line[j].replace(",", ""))) 
            elif(line[0] == "Operation:"):
                if(line[4] == "*"): 
                    monkeys[x].operationOp = 1
                if(line[5] == "old"):  continue
                else: monkeys[x].operationNum = int(line[5]) 
            elif(line[0] == "Test:"):
                monkeys[x].test = int(line[3])      
                product *= int(line[3]) 
            elif(line[0] == "If"): 
                if line[1] == "true:": monkeys[x].throwTrue = int(line[-1]) 
                else: monkeys[x].throwFalse = int(line[-1])

        for x in range(self.taskOneRounds):
            for y in range(len(monkeys)): 
                while(len(monkeys[y].item) > 0): 
                    inspected[y] +=1
                    currentItem = monkeys[y].item.pop(0)
                    if(monkeys[y].operationOp == 0):
                        currentItem += monkeys[y].operationNum 
                    if(monkeys[y].operationOp == 1):
                        if(monkeys[y].operationNum == 0):
                            currentItem*= currentItem
                        else:
                            currentItem *= monkeys[y].operationNum  
                    currentItem //= 3
                    if(currentItem % int(monkeys[y].test) == 0):
                        monkeys[monkeys[y].throwTrue].item.append(currentItem)
                    else:
                        monkeys[monkeys[y].throwFalse].item.append(currentItem)

        inspected = sorted(inspected)    
        return inspected[-2] * inspected[-1] 


    def task_two(self):
        product = 1
        monkeys = [Monkey() for _ in range(self.numMonkeys)] 
        inspected = [0 for _ in range(self.numMonkeys)]
        puzzle_input = self.get_puzzle_input()
        
        x = 0
        for line in puzzle_input[1:]:
            line = line.split()
            if len(line) == 0: continue
            if(line[0] == "Monkey"): x += 1
            elif(line[0] == "Starting"):
                for j in range(2, len(line)):
                    monkeys[x].item.append(int(line[j].replace(",", ""))) 
            elif(line[0] == "Operation:"):
                if(line[4] == "*"): 
                    monkeys[x].operationOp = 1
                if(line[5] == "old"):  continue
                else: monkeys[x].operationNum = int(line[5]) 
            elif(line[0] == "Test:"):
                monkeys[x].test = int(line[3])      
                product *= int(line[3]) 
            elif(line[0] == "If"): 
                if line[1] == "true:": monkeys[x].throwTrue = int(line[-1]) 
                else: monkeys[x].throwFalse = int(line[-1])          

        for x in range(self.taskTwoRounds):
            for y in range(len(monkeys)): 
                while(len(monkeys[y].item) > 0): 
                    inspected[y] +=1
                    currentItem = monkeys[y].item.pop(0)
                    if(monkeys[y].operationOp == 0):
                        currentItem += monkeys[y].operationNum 
                    if(monkeys[y].operationOp == 1):
                        if(monkeys[y].operationNum == 0):
                            currentItem*= currentItem
                        else:
                            currentItem *= monkeys[y].operationNum   
                    currentItem %= product 
                    if(currentItem % monkeys[y].test == 0):
                        monkeys[monkeys[y].throwTrue].item.append(currentItem)
                    else:
                        monkeys[monkeys[y].throwFalse].item.append(currentItem)

        inspected = sorted(inspected)    
        return inspected[-2] * inspected[-1] 


if __name__ == "__main__": 
    s = DayEleven() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
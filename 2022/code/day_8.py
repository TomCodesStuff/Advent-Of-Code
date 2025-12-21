from solution_base import Solution 


class DayEight(Solution):  
    def __init__(self):
        self.viewDistance = 0 
        self.visible = 0 
        self.score = 0 

        self.parse_puzzle_input()


    # Functions
    def check_right(self, trees, i, j): 
        for x in range(j + 1, len(trees[i])): 
            if(trees[i][j] <= trees[i][x]):
                self.viewDistance += 1 
                return 0
            self.viewDistance += 1
        return 1 


    def check_left(self, trees, i, j):
        for x in range(j - 1, -1, -1):
            if(trees[i][j] <= trees[i][x]):
                self.viewDistance += 1
                return 0
            self.viewDistance += 1
        return 1 


    def check_column_down(self, trees, i, j):
        for x in range(i + 1, len(trees)):
            if(trees[i][j] <= trees[x][j]):
                self.viewDistance += 1
                return 0 
            self.viewDistance += 1
        return 1

    def check_column_up(self, trees, i, j): 
        for x in range(i - 1, -1, -1):
            if(trees[i][j] <= trees[x][j]):
                self.viewDistance+=1
                return 0 
            self.viewDistance+=1
        return 1 


    def parse_puzzle_input(self):
        trees = [] 
        for line in self.get_puzzle_input():
            trees.append(list(line)) 

        for i in range(len(trees)):
            for j in range(len(trees[i])):
                if(j == 0 or i == 0 or i == len(trees)-1 or j == len(trees[i]) -1): 
                    self.visible += 1
                else: 
                    if(self.check_right(trees, i, j) == 1): 
                        self.visible += 1  
                        continue
                    elif(self.check_left(trees, i, j) == 1):
                        self.visible += 1
                        continue 
                    elif(self.check_column_down(trees,i,j) == 1):  
                        self.visible += 1 
                        continue 
                    elif(self.check_column_up(trees, i, j) == 1):
                        self.visible += 1
                        continue 

        self.viewDistance = 0 
        tmp = 1
        
        for i in range(len(trees)):
            for j in range(len(trees[i])):
                self.check_right(trees, i,j)
                tmp *= self.viewDistance
                self.viewDistance = 0
                
                self.check_left(trees, i, j)
                tmp *= self.viewDistance
                self.viewDistance = 0  
        
                self.check_column_down(trees, i, j)
                tmp *= self.viewDistance 
                self.viewDistance = 0 
                
                self.check_column_up(trees, i, j)
                tmp *= self.viewDistance
                self.viewDistance = 0
                
                if(tmp > self.score): self.score = tmp 
                tmp = 1 


    def task_one(self): return self.visible
    

    def task_two(self): return self.score


if __name__ == "__main__": 
    s = DayEight() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
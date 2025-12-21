# Is this inefficient? Yes
# Does it work? Somehow
# Did I spend too much time on this? For sure  

# Tom from 2025 here, I'm not touching this with a 20ft barge pole

from solution_base import Solution 


class DayNine(Solution): 

    def task_one(self):
        snake = [[0,0] for _ in range(2)]
        nodesVisited = [[0,0]]
        visited = 1
        for line in self.get_puzzle_input(): 
                line = line.split(" ") 
                if(line[0] == "R"):
                    for _ in range(0, int(line[1])):
                        snake[0][0] += 1
                        if(snake[0][0] - snake[1][0] == 2): 
                            if(snake[0][1] != snake[1][1]):
                                snake[1][1] = snake[0][1]
                            snake[1][0]+=1  
                    
                            if(snake[1] not in nodesVisited):
                                visited+=1
                                nodesVisited.append([snake[1][0],snake[1][1]])
            
                elif(line[0] == "L"):
                    for _ in range(0, int(line[1])):
                        snake[0][0] -= 1 
                        if(snake[1][0] - snake[0][0] == 2):
                            if(snake[1][1] != snake[0][1]):
                                snake[1][1] = snake[0][1]
                            snake[1][0]-=1  
                        
                            if(snake[1] not in nodesVisited):
                                visited+=1
                                nodesVisited.append([snake[1][0],snake[1][1]])
            
                elif(line[0] == "U"):
                    for _ in range(0, int(line[1])):
                        snake[0][1] += 1
                    
                        if(snake[0][1] - snake[1][1] == 2):
                            if(snake[0][0] != snake[1][0]):
                                snake[1][0] = snake[0][0]
                            snake[1][1] = snake[0][1]-1 
                    
                        if(snake[1] not in nodesVisited):
                                visited+=1
                                nodesVisited.append([snake[1][0],snake[1][1]]) 
        
                elif(line[0] == "D"):
                    for _ in range(0, int(line[1])):
                        snake[0][1] -= 1 
                        if(snake[1][1] - snake[0][1] == 2):
                            if(snake[0][0] != snake[1][0]):
                                snake[1][0] = snake[0][0]
                            snake[1][1] = snake[0][1]+1 
                        
                            if(snake[1] not in nodesVisited):
                                visited+=1
                                nodesVisited.append([snake[1][0],snake[1][1]]) 
        return visited             


    # Solution 2
    def task_two(self):
        snake = [[0,0] for _ in range(10)]
        nodesVisited = [[0,0]]
        visited = 1

        for line in self.get_puzzle_input():
                line = line.strip().split(" ")
                for _ in range(int(line[1])):
                    if(line[0] == "R"): snake[0][0] += 1
                    if(line[0] == "L"): snake[0][0] -=1
                    if(line[0] == "U"): snake[0][1] +=1
                    if(line[0] == "D"): snake[0][1] -= 1 

                    for a in range(1, len(snake)):
                        if(snake[a-1][0] - snake[a][0] >= 2):
                            snake[a][0] +=1 
                            if(snake[a-1][1] - snake[a][1] == 2):
                                snake[a][1] +=1
                            elif(snake[a][1] - snake[a-1][1] >= 2):
                                    snake[a][1]-=1  
                            elif(snake[a][1] != snake[a-1][1]):
                                snake[a][1] = snake[a-1][1]
                        
                        elif(snake[a][0] - snake[a-1][0] >= 2):
                                snake[a][0] -=1 
                                if(snake[a-1][1] - snake[a][1] == 2):
                                    snake[a][1]+=1 
                                elif(snake[a][1] - snake[a-1][1] >= 2):
                                    snake[a][1]-=1  
                                elif(snake[a][1] != snake[a-1][1]):
                                    snake[a][1] = snake[a-1][1]

                        elif(snake[a-1][1] - snake[a][1] >=2): 
                                snake[a][1] +=1
                                if(snake[a-1][0] - snake[a][0] >= 2):
                                    snake[a][0]+=1  
                                elif(snake[a][0] - snake[a-1][0] >= 2):
                                    snake[a][0]-=1 
                                elif(snake[a][0] != snake[a-1][0]):
                                    snake[a][0] = snake[a-1][0]
                            
                        elif(snake[a][1] - snake[a-1][1] >=2): 
                                snake[a][1] -=1  
                                if(snake[a-1][0] - snake[a][0] >= 2):
                                    snake[a][0] +=1
                                elif(snake[a][0] - snake[a-1][0] >= 2):
                                    snake[a][0]-=1  
                                elif(snake[a][0] != snake[a-1][0]):
                                    snake[a][0] = snake[a-1][0] 
                        
                    if(snake[9] not in nodesVisited):
                        visited+=1
                        nodesVisited.append([snake[9][0], snake[9][1]]) 
        return visited 


if __name__ == "__main__": 
    s = DayNine() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
# Not so elegant Dijkstra's shortest path
# self.maxVal was chosen to represent infinity since it's large enough to work
# And it's over self.maxVal 

# Tom from 2025, use math.inf 

from solution_base import Solution 


class Node:
    def __init__(self, numVal, charVal, weight):
        self.numVal = numVal
        self.charVal = charVal
        self.distance = weight
        self.next = []
        self.visited = 0


class DayOne(Solution):  
    def __init__(self):
        self.taskOneDest = "S"
        self.taskTwoDest = "E"
        self.maxVal = 9000


    def neighbours_task_one(self, graph, node, x, y):
        if(y == 0):
            if(graph[x][y+1].numVal <= node.numVal + 1):
                node.next.append(graph[x][y+1]) 
        elif(y == len(graph[x]) - 1):
            if(graph[x][y-1].numVal <= node.numVal + 1):
                node.next.append(graph[x][y-1]) 
        else: 
            if(graph[x][y-1].numVal <= node.numVal + 1):
                node.next.append(graph[x][y-1])
            if(graph[x][y+1].numVal <= node.numVal + 1):
                node.next.append(graph[x][y+1]) 

        if(x == 0):
            if(graph[x+1][y].numVal <= node.numVal + 1):
                node.next.append(graph[x+1][y])  
        elif(x == len(graph) - 1):
            if(graph[x-1][y].numVal <= node.numVal + 1):
                node.next.append(graph[x-1][y])   
        else:
            if(graph[x+1][y].numVal <= node.numVal + 1):
                node.next.append(graph[x+1][y]) 
            if(graph[x-1][y].numVal <= node.numVal + 1):
                node.next.append(graph[x-1][y])   


    def task_one(self):  
        graph = [list(line) for line in self.get_puzzle_input()]
        
        nodeQueue = []
        for a in range(len(graph)):
            for b in range(len(graph[a])):
                if(graph[a][b] == self.taskOneDest):
                    graph[a][b] = (Node(97,graph[a][b],0)) 
                    nodeQueue.append(graph[a][b])
                elif(graph[a][b] == "E"):
                    graph[a][b] = (Node(122,graph[a][b], self.maxVal)) 
                    nodeQueue.append(graph[a][b])
                else:
                    graph[a][b] = (Node(ord(graph[a][b]), graph[a][b], self.maxVal))
                    nodeQueue.append(graph[a][b])
                    
        for a in range(len(graph)):
            for b in range(len(graph[a])):
                self.neighbours_task_one(graph, graph[a][b], a, b)
        
        while(nodeQueue): 
            min = self.maxVal + 1
            for a in range(len(nodeQueue)):
                if(nodeQueue[a].distance < min):
                    min = nodeQueue[a].distance
                    visiting = nodeQueue[a] 
                    remove = a
            for b in range(len(visiting.next)): 
                if(visiting.visited == 1): continue
                tmpDist = visiting.distance + 1
                if(tmpDist < visiting.next[b].distance):
                    visiting.next[b].distance = tmpDist
            nodeQueue.pop(remove)
            visiting.visited = 1
            if(visiting.charVal == "E"):
                return visiting.distance


    def neighbours_task_two(self, graph, node, x, y):
        if(y == 0):
            if(graph[x][y+1].numVal >= node.numVal - 1):
                node.next.append(graph[x][y+1]) 
        elif(y == len(graph[x]) - 1):
            if(graph[x][y-1].numVal >= node.numVal - 1):
                node.next.append(graph[x][y-1]) 
        else: 
            if(graph[x][y-1].numVal >= node.numVal - 1):
                node.next.append(graph[x][y-1])
            if(graph[x][y+1].numVal >= node.numVal - 1):
                node.next.append(graph[x][y+1]) 

        if(x == 0):
            if(graph[x+1][y].numVal >= node.numVal - 1):
                node.next.append(graph[x+1][y])  
        elif(x == len(graph) - 1):
            if(graph[x-1][y].numVal >= node.numVal - 1):
                node.next.append(graph[x-1][y])   
        else:
            if(graph[x+1][y].numVal >= node.numVal - 1):
                node.next.append(graph[x+1][y])  
            if(graph[x-1][y].numVal >= node.numVal - 1):
                node.next.append(graph[x-1][y])   

        
    def task_two(self):
        graph = [list(line) for line in self.get_puzzle_input()]
        nodeQueue = []
        for a in range(len(graph)):
            for b in range(len(graph[a])):
                if(graph[a][b] == self.taskTwoDest):
                    graph[a][b] = (Node(122,graph[a][b],0)) 
                    nodeQueue.append(graph[a][b])
                elif(graph[a][b] == "S"):
                    graph[a][b] = (Node(97,graph[a][b], self.maxVal)) 
                    nodeQueue.append(graph[a][b])
                else:
                    graph[a][b] = (Node(ord(graph[a][b]), graph[a][b], self.maxVal))
                    nodeQueue.append(graph[a][b])
                    
        for a in range(len(graph)):
            for b in range(len(graph[a])):
                self.neighbours_task_two(graph, graph[a][b], a, b)
        
        lowest = self.maxVal
        while(nodeQueue): 
            min = self.maxVal + 1
            for a in range(len(nodeQueue)):
                if(nodeQueue[a].distance < min):
                    min = nodeQueue[a].distance
                    visiting = nodeQueue[a] 
                    remove = a
            for b in range(len(visiting.next)): 
                if(visiting.visited == 1): continue
                tmpDist = visiting.distance + 1
                if(tmpDist < visiting.next[b].distance):
                    visiting.next[b].distance = tmpDist
            nodeQueue.pop(remove)
            visiting.visited = 1
            if(visiting.charVal == "a" and visiting.distance < lowest):
                lowest = visiting.distance
        return lowest


if __name__ == "__main__": 
    s = DayOne() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
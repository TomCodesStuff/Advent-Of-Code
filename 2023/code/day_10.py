import math
from solution_base import Solution 

# TODO clean up repeated code

class DayTen(Solution): 


    def find_loop(self, startPos, pipes, tiles, direction):
        loopLength = 0
        visited = []
        y,x = startPos  
        while(loopLength == 0 or (y,x) != startPos): 
            visited.append((y,x))
            char = pipes[(y, x)]
            y += direction[0]
            x += direction[1]
            if(pipes[y, x] in tiles[char][direction]): return 0, 0
            if(pipes[(y,x)] == "S"): return (loopLength, visited)
            if((y,x) in visited): return 0, 0 
            if(pipes[(y,x)] == "."): return 0, 0 
            if((y,x) not in pipes): return 0, 0
            loopLength += 1
            if(pipes[(y , x)] == "7"):
                if(direction == (0, 1)):
                    direction = (1, 0) 
                else: direction = (0, -1)
            elif(pipes[(y, x)] == "F"):
                if(direction == (0 , -1)):
                    direction = (1, 0)
                else: direction = (0, 1)
            elif(pipes[y, x] == "J"):
                if(direction == (0, 1)):
                    direction = (-1, 0)
                else: direction = (0, -1)
            elif(pipes[y,x] == "L"):
                if(direction == (1, 0)):
                    direction = (0, 1)
                else: direction = (-1, 0)
        return (loopLength, visited)


    def task_one(self):
        pipes = {}

        for y, line in enumerate(self.get_puzzle_input()):
            for x, char in enumerate(line):
                pipes[(y,x)] = char  
                if(char == "S"): start = (y,x)
        
        tiles = {
            "-": {(0, 1) : ["|", "L", "F"], (0, -1): ["|", "J", "7"]},
            "|": {(-1,0) : ["-", "L", "J"], (1 , 0) : ["-", "F", "7"]},
            "L": {(-1, 0) : ["-", "J", "L"], (0, 1): ["|", "F", "L"]},
            "J": {(0, -1) : ["|", "7", "J"], (-1, 0) : ["-", "L", "J"]},
            "7": {(0, -1) : ["7", "|", "J"], (1, 0): ["7", "-", "F"]},
            "F": {(1, 0) : ["-", "7", "F"],(0, 1):  ["|", "F", "L"]},
            ".": [],
            "S" : {(1, 0): ["-", "F", "7"], (-1, 0) : ["-", "L", "J"], (0, 1) : ["L", "F", "|"], (0, -1) : ["|", "J", "7"]}
        }
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            (loopLength, _) = self.find_loop(start, pipes, tiles, direction)
            if(loopLength): return math.ceil(loopLength / 2)


    def shoelace(self, loop):
        sum = 0 
        for i in range(len(loop) - 1): 
            y,x = loop[i]
            y2, x2 = loop[i + 1] 
            sum += (y + y2) * (x - x2)
        y, x = loop[-1]
        y2, x2 = loop[0]
        sum += (y + y2) * (x - x2)
        return abs(sum / 2)


    def task_two(self):
        pipes = {}

        for y, line in enumerate(self.get_puzzle_input()):
            for x, char in enumerate(line):
                pipes[(y,x)] = char  
                if(char == "S"): start = (y,x)
        
        tiles = {
            "-": {(0, 1) : ["|", "L", "F"], (0, -1): ["|", "J", "7"]},
            "|": {(-1,0) : ["-", "L", "J"], (1 , 0) : ["-", "F", "7"]},
            "L": {(-1, 0) : ["-", "J", "L"], (0, 1): ["|", "F", "L"]},
            "J": {(0, -1) : ["|", "7", "J"], (-1, 0) : ["-", "L", "J"]},
            "7": {(0, -1) : ["7", "|", "J"], (1, 0): ["7", "-", "F"]},
            "F": {(1, 0) : ["-", "7", "F"],(0, 1):  ["|", "F", "L"]},
            ".": [],
            "S" : {(1, 0): ["-", "F", "7"], (-1, 0) : ["-", "L", "J"], (0, 1) : ["L", "F", "|"], (0, -1) : ["|", "J", "7"]}
        }
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            (loopLength, loop) = self.find_loop(start, pipes, tiles, direction)
            if(loopLength): break 
        return math.floor(self.shoelace(loop) - (loopLength / 2) + 1) 


if __name__ == "__main__": 
    s = DayTen() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
# This one might take a while, so grab a coffee or something
# A friend helped with part 2 because I was very stuck
 
import re
from solution_base import Solution 


class DayFifteen(Solution): 
    def __init__(self):
        self.maxRow = 2000000
        self.tuningFreqConstant = 4000000


    # Solution 1
    def task_one(self):
        beacons = set()
        sensors = []
        nobeacons = set() 
        y = self.maxRow

        for line in self.get_puzzle_input():
            line = re.split("=|:|,", line.strip())

            xOrd = int(line[1])
            yOrd = int(line[3])  
            bx = int(line[5])
            by = int(line[-1])   

            manDist = abs(xOrd - bx) + abs(yOrd - by)  
            sensors.append([(xOrd, yOrd), manDist])
            
            if(by == y):
                beacons.add((bx, by)) 

        i = 0
        while(i < len(sensors)):
            manDist = sensors[i][1]
            xCord = sensors[i][0][0]
            yCord = sensors[i][0][1]
            if(yCord + manDist < y):
                i+=1 
                continue
            elif(yCord - manDist > y):
                i+=1
                continue
            else:
                if(yCord < y):
                    for c in range(manDist - (y - yCord) + 1):
                        if((xCord + c, y) not in beacons):
                            nobeacons.add((xCord + c, y)) 
                        if((xCord - c, y) not in beacons):
                            nobeacons.add((xCord - c, y))
                elif(yCord > y):
                    for c in range(manDist + (y - yCord) + 1):
                        if((xCord + c, y) not in beacons):
                            nobeacons.add((xCord + c, y)) 
                        if((xCord - c, y) not in beacons):
                            nobeacons.add((xCord - c, y))
                else:
                    for c in range(manDist + 1):
                        if((xCord + c, y) not in beacons):
                            nobeacons.add((xCord + c, y)) 
                        if((xCord - c, y) not in beacons):
                            nobeacons.add((xCord - c, y))
            i+=1
        return len(nobeacons)

    # Solution 2
    def task_two(self):
        print("WARNING: Task Two takes ~90 seconds to finish!")
        sensors = []

        for line in self.get_puzzle_input():
            line = re.split("=|:|,", line.strip())
            xOrd = int(line[1])
            yOrd = int(line[3])  
            bx = int(line[5])
            by = int(line[-1])   
            manDist = abs(xOrd - bx) + abs(yOrd - by)  
            sensors.append([[xOrd, yOrd], manDist])
        
        y  = 0
        while(y <= self.tuningFreqConstant):
            x = 0 
            while(x <= self.tuningFreqConstant):
                beacon = True
                for sensor in sensors:
                    if(abs(sensor[0][0] - x) + abs(sensor[0][1] - y) <= sensor[1]):
                        x = sensor[0][0] + (sensor[1] - abs(sensor[0][1] - y))
                        beacon = False
                        break
                if(beacon):
                    return x* self.tuningFreqConstant + y
                x+=1
            y+=1


if __name__ == "__main__": 
    s = DayFifteen() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
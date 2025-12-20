import math
import re
from solution_base.solution import Solution 


class DayFive(Solution): 


    def parse_seeds(self, line):
        return re.sub("[a-zA-Z]+[:]+[ ]", "", line).split(" ") 


    def parse_puzzle_input(self):
        puzzle_input = self.get_puzzle_input()
        seeds = self.parse_seeds(puzzle_input[0]) 

        almanacRegex = "[0-9]+ [0-9]+ [0-9]+"
        gardenMappings = [[]]
        i = 0

        for line in puzzle_input[2:]: 
            mapping_match = re.match(almanacRegex, line)
            if mapping_match: 
                a, b, c = map(int, mapping_match.group().split(" "))
                gardenMappings[i].append([b, b + c - 1, a - b])
            elif line == "": 
                gardenMappings[i].sort()
                gardenMappings.append([])
                i += 1 
        
        return (seeds, gardenMappings)


    def parse_map(filePtr):
        spaceCount = 0
        numLst = []
        while(spaceCount < 1):
            line = filePtr.readline()
            if(line == "\n" or line == ""): spaceCount += 1
            if(re.match("[0-9]", line)):
                nums = line.rstrip().split(" ")
                numLst.append([int(nums[1]), int(nums[1]) + int(nums[2]) - 1, int(nums[0]) - int(nums[1])]) 
        return sorted(numLst)


    def binary_search(self, lst, val):
        low = 0 
        high = len(lst) - 1
        while(low <= high): 
            mid = (low + high) // 2
            if(val < lst[mid][0]): 
                high = mid - 1
            elif(val > lst[mid][1]):
                low = mid + 1  
            else: return mid 
        return -1


    def map_values(self, lst, mappedVal):
        index = self.binary_search(lst, mappedVal)
        if (index != -1): return mappedVal + lst[index][2] 
        return mappedVal


    def task_one(self):
        seeds, gardenMappings = self.parse_puzzle_input()
        lowestLocation = math.inf
        for seed in seeds:
            mappedVal = int(seed) 
            for mapping in gardenMappings:
                mappedVal = self.map_values(mapping, mappedVal)     
            lowestLocation = min(lowestLocation, mappedVal)      
        return lowestLocation


    def parse_seed_ranges(self, seeds):
        seed_ranges = []
        for i in range(0, len(seeds) - 1, 2): 
            seed_ranges.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1])
        return sorted(seed_ranges)


    def split_ranges(self, splitLst, checkLst):
        i = 0 
        while(i < len(splitLst)):
            for j in range(0, len(checkLst)):
                if(splitLst[i][0] > checkLst[j][1]): continue
                if(splitLst[i][1] < checkLst[j][0]): continue
                if(splitLst[i][0] >= checkLst[j][0] and splitLst[i][1] > checkLst[j][1]): 
                    splitLst.append([checkLst[j][1] + 1, splitLst[i][1]])
                    splitLst[i][1] = checkLst[j][1]
                elif(splitLst[i][0] < checkLst[j][0] and splitLst[i][1] <= checkLst[j][1]):
                    splitLst.append([splitLst[i][0], checkLst[j][0] - 1])
                    splitLst[i][0] = checkLst[j][0]
                splitLst[i][0] += checkLst[j][2]
                splitLst[i][1] += checkLst[j][2] 
                break 
            i+=1
        return splitLst


    def task_two(self): 
        seeds, gardenMappings = self.parse_puzzle_input()  
        seeds = self.parse_seed_ranges(seeds)
        mappedVal = seeds
        for mapping in gardenMappings: 
            mappedVal = self.split_ranges(mappedVal, mapping)
        mappedVal.sort()
        return mappedVal[0][0]


if __name__ == "__main__": 
    s = DayFive() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")

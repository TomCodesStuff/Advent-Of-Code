from solution_base.solution import Solution 


class DayEleven(Solution): 


    def task_one(self):
        galaxies = []
        emptyRows = []
        
        puzzle_input = self.get_puzzle_input()
        columnsGalaxyCount = [0 for _ in range(len(puzzle_input))]
        
        for i, line in enumerate(puzzle_input):
            galaxyCount = 0
            for j, char in enumerate(line):
                if(char == "#"): 
                    galaxyCount += 1
                    galaxies.append([i, j]) 
                    columnsGalaxyCount[j] += 1
            if(galaxyCount == 0): emptyRows.append(i) 
        
        emptyColumns = [index for index, i in enumerate(columnsGalaxyCount) if i == 0]
        for galaxy in galaxies:
            rowIncrease = 0
            columnIncrease = 0
            for column in emptyColumns:
                if(galaxy[1] > column): columnIncrease += 1
            for row in emptyRows: 
                if(galaxy[0] > row): rowIncrease += 1
            galaxy[0] += rowIncrease
            galaxy[1] += columnIncrease 
        
        total = 0
        n = len(galaxies)
        for i in range(n):
            for j in range(i + 1, n):
                total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) 
        return total


    def task_two(self):
        galaxies = []
        emptyRows = []
        
        puzzle_input = self.get_puzzle_input()
        columnsGalaxyCount = [0 for _ in range(len(puzzle_input))]
        for i, line in enumerate(puzzle_input):
            galaxyCount = 0
            for j, char in enumerate(line.rstrip()):
                if(char == "#"): 
                    galaxyCount += 1
                    galaxies.append([i, j]) 
                    columnsGalaxyCount[j] += 1
            if(galaxyCount == 0): emptyRows.append(i) 
        
        emptyColumns = [index for index, i in enumerate(columnsGalaxyCount) if i == 0]
        for galaxy in galaxies:
            rowIncrease = 0
            columnIncrease = 0
            for column in emptyColumns:
                if(galaxy[1] > column): columnIncrease += 999999
            for row in emptyRows: 
                if(galaxy[0] > row): rowIncrease += 999999
            galaxy[0] += rowIncrease
            galaxy[1] += columnIncrease 
        
        total = 0
        n = len(galaxies)
        for i in range(n):
            for j in range(i + 1, n):
                total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) 
        return total 


if __name__ == "__main__": 
    s = DayEleven() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
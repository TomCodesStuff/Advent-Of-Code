from solution_base.solution import Solution 

# TODO repeated code in parts one + two can be merged 

class DayThree(Solution): 


    def get_number(self, index, engineArray, lineNumber, lineLength):
        number = engineArray[lineNumber][index]
        left = index - 1
        while(left >= 0 and engineArray[lineNumber][left].isnumeric()):
            number = engineArray[lineNumber][left] + number
            left -= 1
        right = index + 1
        while(right < lineLength and engineArray[lineNumber][right].isnumeric()):
            number += engineArray[lineNumber][right] 
            right += 1
        return int(number)


    def check_left(self, symbolIndex, lineNumber, engineArray):    
        if(symbolIndex == 0): return False
        if(engineArray[lineNumber][symbolIndex - 1].isnumeric()): 
            return True
        else: return False  


    def check_right(self, symbolIndex, lineNumber, engineArray, lineLength):
        if(symbolIndex == lineLength - 1): return False
        if(engineArray[lineNumber][symbolIndex + 1].isnumeric()): 
            return True
        else: return False  


    def check_up(self, symbolIndex, lineNumber, engineArray): 
        if(lineNumber == 0): return False
        if(engineArray[lineNumber - 1][symbolIndex].isnumeric()): 
            return True
        else: return False  


    def check_down(self, symbolIndex, lineNumber, engineArray, numberLines):
        if(lineNumber == numberLines - 1): return False
        if(engineArray[lineNumber + 1][symbolIndex].isnumeric()): 
            return True
        else: return False  


    def task_one(self):
        total = 0
        numberLines = 0 
        lineNumber = 0 
        lineLength = 0
        engineArray = []
        symbolsArray = []
        

        for line in self.get_puzzle_input():
            engineArray.append([])
            symbolsArray.append([])
            for index, char in enumerate(line):
                if(not char.isnumeric() and char != "."):
                    symbolsArray[lineNumber].append(index)
                engineArray[lineNumber].append(char)
            lineNumber+=1
            numberLines+=1 

        lineLength = len(line)
        lineNumber = -1
        
        for i in range(len(symbolsArray)):
            lineNumber+=1
            if(symbolsArray[i] == []): continue
            for j in range(len(symbolsArray[i])):
                if(self.check_left(symbolsArray[i][j], i, engineArray)):
                    total += self.get_number(symbolsArray[i][j] - 1, engineArray, i, lineLength)
                if(self.check_right(symbolsArray[i][j], i, engineArray, lineLength)):
                    total += self.get_number(symbolsArray[i][j] + 1, engineArray, i, lineLength)
                if(self.check_up(symbolsArray[i][j], i, engineArray)):
                    total += self.get_number(symbolsArray[i][j], engineArray, i - 1, lineLength)
                else:
                    if(self.check_left(symbolsArray[i][j], i - 1, engineArray)): 
                        total  += self.get_number(symbolsArray[i][j] - 1, engineArray, i - 1, lineLength)
                    if(self.check_right(symbolsArray[i][j], i - 1, engineArray, lineLength)):
                        total += self.get_number(symbolsArray[i][j] + 1, engineArray, i - 1, lineLength)
                if(self.check_down(symbolsArray[i][j], lineNumber, engineArray, numberLines)):
                    total += self.get_number(symbolsArray[i][j], engineArray, i + 1, lineLength)
                else:
                    if(self.check_left(symbolsArray[i][j], i + 1, engineArray)): 
                        total += self.get_number(symbolsArray[i][j] - 1, engineArray, i + 1, lineLength)
                    if(self.check_right(symbolsArray[i][j], i + 1, engineArray, lineLength)):
                        total += self.get_number(symbolsArray[i][j] + 1, engineArray, i + 1, lineLength)
        return total


    def task_two(self):
        total = 0
        numberLines = 0 
        lineNumber = 0 
        lineLength = 0
        engineArray = []
        gearsArray = []
        
        for line in self.get_puzzle_input():
            engineArray.append([])
            gearsArray.append([])
            for index, char in enumerate(line):
                if(char == "*"):
                    gearsArray[lineNumber].append(index)
                engineArray[lineNumber].append(char)
            lineNumber+=1
            numberLines+=1 
        
        lineLength = len(line)
        lineNumber = -1
        
        for i in range(len(gearsArray)):
            lineNumber+=1
            if(gearsArray[i] == []): continue
            for j in range(len(gearsArray[i])):
                numAdjGear = 0
                ratio = 1
                if(self.check_left(gearsArray[i][j], i, engineArray)):
                    ratio *= self.get_number(gearsArray[i][j] - 1, engineArray, i, lineLength)
                    numAdjGear += 1
                if(self.check_right(gearsArray[i][j], i, engineArray, lineLength)):
                    ratio *= self.get_number(gearsArray[i][j] + 1, engineArray, i, lineLength)
                    numAdjGear += 1
                if(self.check_up(gearsArray[i][j], i, engineArray)):
                    ratio *= self.get_number(gearsArray[i][j], engineArray, i - 1, lineLength)
                    numAdjGear += 1
                else:
                    if(self.check_left(gearsArray[i][j], i - 1, engineArray)): 
                        ratio *= self.get_number(gearsArray[i][j] - 1, engineArray, i - 1, lineLength)
                        numAdjGear += 1
                    if(self.check_right(gearsArray[i][j], i - 1, engineArray, lineLength)):
                        ratio *= self.get_number(gearsArray[i][j] + 1, engineArray, i - 1, lineLength)
                        numAdjGear += 1
                if(self.check_down(gearsArray[i][j], lineNumber, engineArray, numberLines)):
                    ratio *= self.get_number(gearsArray[i][j], engineArray, i + 1, lineLength)
                    numAdjGear += 1
                else:
                    if(self.check_left(gearsArray[i][j], i + 1, engineArray)): 
                        ratio *= self.get_number(gearsArray[i][j] - 1, engineArray, i + 1, lineLength)
                        numAdjGear += 1
                    if(self.check_right(gearsArray[i][j], i + 1, engineArray, lineLength)):
                        ratio *= self.get_number(gearsArray[i][j] + 1, engineArray, i + 1, lineLength)
                        numAdjGear += 1
                if(numAdjGear == 2): 
                    total += ratio
        return total    


if __name__ == "__main__": 
    s = DayThree() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")

from solution_base import Solution 


class DayFour(Solution): 


    # Solution one
    def task_one(self):

        # Gets values from line and seperates by space, each word is j, can be used for ints to 
        i, j, total = 0, 0, 0
        
        for line in self.get_puzzle_input():  
                i, j = 0, 0  
                data = line.split(",")
                
                dataStr = str(data[0])
                while(dataStr[i] != "-"):
                    j += 1 
                    i += 1
                
                i = 0  
                firstRangeL = int(dataStr[:j])
                firstRangeH = int(dataStr[j+1:])
                dataStr = str(data[1]) 
                j = 0
                
                while(dataStr[i] != "-"):
                    j += 1
                    i+=1  
                
                secondRangeL = int(dataStr[:j])
                secondRangeH = int(dataStr[j+1:])  
                
                if(firstRangeL >= secondRangeL and firstRangeH <= secondRangeH): total +=1 
                elif(secondRangeL >= firstRangeL and secondRangeH <= firstRangeH): total +=1
        return total


    # Solution 2
    def task_two(self):
        # Gets values from line and seperates by space, each word is j, can be used for ints to 
        i, j, total = 0, 0, 0 

        for line in self.get_puzzle_input(): 
            i, j = 0, 0
            data = line.strip().split(",")
            
            
            dataStr = str(data[0])
            while(dataStr[i] != "-"):
                i +=1
                j += 1
            
            
            i = 0  
            firstRangeL = int(dataStr[:j])
            firstRangeH = int(dataStr[j + 1:])
            j = 0
            
            dataStr = str(data[1])
            while(dataStr[i] != "-"):
                i+=1  
                j+=1
            
            secondRangeL = int(dataStr[:j])
            secondRangeH = int(dataStr[j+1:])  
            
            if(firstRangeL >= secondRangeL and firstRangeH <= secondRangeH): total  +=1 
            elif(secondRangeL >= firstRangeL and secondRangeH <= firstRangeH): total +=1
            elif(firstRangeH - secondRangeL >=0 and firstRangeH - secondRangeH <= 0): total +=1
            elif(secondRangeH - firstRangeL >=0 and secondRangeH - firstRangeH <= 0): total +=1
        return total 
  

if __name__ == "__main__": 
    s = DayFour() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
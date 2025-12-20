from solution_base import Solution 


class DayTwo(Solution): 


    # Solution 1
    def task_one(self):
        rps = []  

        for line in self.get_puzzle_input(): 
                data = line.split(" ") 
                for n in data: rps.append(n)
        
        score = 0   
        i = 0
        while(i < len(rps)): 
            if(rps[i] == 'A' and rps[i+1] == 'Y'):
                score+=8
            elif(rps[i] == 'B' and rps[i+1] == 'Z'):
                score+=9
            elif(rps[i] == 'C' and rps[i+1] == 'X'):
                score+=7
            elif(rps[i] == 'A' and rps[i+1] == 'X'):
                score+=4
            elif(rps[i] == 'B' and rps[i+1] == 'Y'):
                score+=5
            elif(rps[i] == 'C' and rps[i+1] == 'Z'):
                score+=6
            elif(rps[i] == 'A' and rps[i+1] == 'Z'):
                score+=3
            elif(rps[i] == 'B' and rps[i+1] == 'X'):
                score+=1
            elif(rps[i] == 'C' and rps[i+1] == 'Y'):
                score+=2
            i+=2
        return score


    # Solution 2 
    def task_two(self):
        rps = []
        for line in self.get_puzzle_input(): 
                data = line.split(" ") 
                for n in data: rps.append(n)
        
        score = 0
        i = 0
        while(i < len(rps)): 
            if(rps[i + 1] == 'X'):
                if(rps[i] == 'A'):
                    score+=3
                elif(rps[i] == 'B'):
                    score+=1
                elif(rps[i] == 'C'):
                    score+=2
            elif(rps[i+1] == 'Y'):
                if(rps[i] == 'A'):
                    score+=4
                elif(rps[i] == 'B'):
                    score+=5
                elif(rps[i] == 'C'):
                    score+=6 
            elif(rps[i + 1] == 'Z'):
                if(rps[i] == 'A'):
                    score+=8
                elif(rps[i] == 'B'):
                    score+=9
                elif(rps[i] == 'C'):
                    score+=7
            i+=2 
        return score


if __name__ == "__main__": 
    s = DayTwo() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")


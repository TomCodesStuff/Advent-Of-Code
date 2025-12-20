from solution_base import Solution 


class DayThree(Solution):  
    def __init__(self):
        #Dictionary to hold lower case letters and subsequent values
        self. alphabet = {
            "a": 1, "b": 2, "c": 3, "d": 4, 
            "e": 5, "f": 6, "g": 7, "h": 8, 
            "i": 9, "j": 10, "k": 11, "l": 12, 
            "m": 13, "n": 14, "o": 15, "p": 16, 
            "q": 17, "r": 18, "s": 19, "t": 20, 
            "u": 21, "v": 22, "w": 23, "x": 24, 
            "y": 25, "z": 26
        }


    # Solution 1
    def task_one(self):
        total = 0
        # Iterate through each line of the file
        for line in self.get_puzzle_input():            
            # Get length of line -> split line in half
            halfway = len(line)//2            
            firstHalf = list(line[:halfway])
            secondHalf = list(line[halfway:])
            
            # Place first half and last half of line into seperate sets
            s= {*firstHalf}
            a = {*secondHalf}
            
            # Get the intersect (Shared value) of these sets
            intersect = s.intersection(a)
            interVal = intersect.pop()
            
            # If the value is a capital, add 26 to corresponding lower case in the dictionary 
            if(interVal.isupper()):
                interVal = interVal.lower()
                total += self.alphabet[interVal] + 26
            else: total += self.alphabet[interVal]

            # Clear sets and lists
            s.clear()
            a.clear()
            firstHalf.clear()
            secondHalf.clear() 
        return total
    

    # Solution 2
    def task_two(self):
        k, total = 0, 0 
        
        
        puzzle_input = self.get_puzzle_input()
        # Iterates until end of the list
        while(k < len(puzzle_input)):
            # Remove \n and places in a set
            data = puzzle_input[k].strip()  
            a = {*data}
            data = puzzle_input[k+1].strip()  
            b = {*data}
            data = puzzle_input[k+2].strip()  
            c = {*data}
            # Gets intersect of all three sets
            intersect = a.intersection(b,c)
            interVal = intersect.pop() 
            # If the value is a capital, add 26 to corresponding lower case in the dictionary 
            if(interVal.isupper()):
                interVal = interVal.lower()
                total += self.alphabet[interVal] + 26
            else:
                total += self.alphabet[interVal]
            # Clear sets and lists
            a.clear()
            b.clear()
            c.clear()
            k+=3
        
        return total


if __name__ == "__main__": 
    s = DayThree() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
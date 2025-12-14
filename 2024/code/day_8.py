from solution_base.solution import Solution 


class DayEight(Solution):


    def parse_input(self):  
        antenna_coords = {}
        boundaries = {}
        boundaries["min_x"] = 0
        boundaries["min_y"] = 0 

        for i, line in enumerate(self.get_puzzle_input()):
            for j, char in enumerate(line.strip()):
                if char == ".": continue
                if char not in antenna_coords:
                    antenna_coords[char] = [(j, i)]
                else: antenna_coords[char].append((j, i)) 
        boundaries["max_x"] = len(line) - 1
        boundaries["max_y"] = j 
        return (list(antenna_coords.values()), boundaries)


    def validate_antinode(self, antinode, boundaries):
        x, y = antinode
        if(x < boundaries["min_x"] or x > boundaries["max_x"]):
            return False
        if(y < boundaries["min_y"] or y > boundaries["max_y"]):
            return False 
        return True

        
    def task_one(self):
        antenna_coords, boundaries = self.parse_input() 
        antinodes = set()
        for coords in antenna_coords:
            for i, main_antenna in enumerate(coords):
                for check_antenna in coords[i + 1:]: 
                    antenna_dist = tuple(x - y for x, y in zip(main_antenna, check_antenna)) 
                    antinode = tuple(x + y for x, y in zip(main_antenna, antenna_dist))  
                    if(self.validate_antinode(antinode, boundaries)):
                        antinodes.add(antinode)
                    antinode = tuple(x + -y for x, y in zip(check_antenna, antenna_dist)) 
                    if(self.validate_antinode(antinode, boundaries)):
                        antinodes.add(antinode) 
        return len(antinodes)


    def task_two(self): 
        antenna_coords, boundaries = self.parse_input() 
        antinodes = set()
        for coords in antenna_coords: 
            for i, main_antenna in enumerate(coords):
                for check_antenna in coords[i + 1:]: 
                    antinodes.add(main_antenna)
                    antinodes.add(check_antenna)
                    antenna_dist = tuple(x - y for x, y in zip(main_antenna, check_antenna)) 
                    antinode = tuple(x + y for x, y in zip(main_antenna, antenna_dist))  
                    while(self.validate_antinode(antinode, boundaries)):
                        antinodes.add(antinode)
                        antinode = tuple(x + y for x, y in zip(antinode, antenna_dist))  
                    antinode = tuple(x - y for x, y in zip(main_antenna, antenna_dist))  
                    while(self.validate_antinode(antinode, boundaries)):
                        antinodes.add(antinode)
                        antinode = tuple(x - y for x, y in zip(antinode, antenna_dist)) 
        return len(antinodes)


if __name__ == "__main__": 
    s = DayEight() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
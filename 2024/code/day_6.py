from solution_base import Solution 


class DaySix(Solution):


    def parse_input(self):  
        obstr_coords = set()
        start_coords = None
        max_x, max_y = 0, 0
        for i, line in enumerate(self.get_puzzle_input()): 
            for j, char in enumerate(line.strip()):
                if(char == "#"): obstr_coords.add((j, i))
                if(char == "^"): start_coords = (j, i) 
        max_x = len(line) - 1
        max_y = j
        return (start_coords, obstr_coords, max_x, max_y)


    def apply_move(self, current_coords, direction):
        return tuple(x + y for x, y in zip(current_coords, direction))


    def reverse_move(self, current_coords, direction):
        return tuple(x - y for x, y in zip(current_coords, direction))


    def walk_route(self, current_coords, obstr_coords, max_x, max_y):  
        dir_idx = 0
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] 
        route_visited = {current_coords: [directions[dir_idx]]}
        while(True):
            current_coords = self.apply_move(current_coords, directions[dir_idx])
            while(current_coords in obstr_coords):
                current_coords = self.reverse_move(current_coords, directions[dir_idx])
                dir_idx = (dir_idx + 1) % 4
                current_coords = self.apply_move(current_coords, directions[dir_idx])

            x, y = current_coords
            if(x < 0 or x > max_x): break 
            if(y < 0 or y > max_y): break 
    
            if(current_coords in route_visited): 
                if directions[dir_idx] in route_visited[current_coords]:
                    return -1 
                route_visited[current_coords].append(directions[dir_idx])
            else:
                route_visited[current_coords] = [directions[dir_idx]] 
        return route_visited

            
    def task_one(self):
        current_coords, obstr_coords, max_x, max_y = self.parse_input() 
        return len(self.walk_route(current_coords, obstr_coords, max_x, max_y))
            

    def task_two(self): 
        start_coords, obstr_coords, max_x, max_y = self.parse_input() 
        distinct_route = self.walk_route(start_coords, obstr_coords, max_x, max_y)
        del distinct_route[start_coords]
        count = 0
        for coords in distinct_route.keys():
            obstr_coords.add(coords)
            if(self.walk_route(start_coords, obstr_coords, max_x, max_y) == -1): 
                count += 1
            obstr_coords.remove(coords)  
        return count


if __name__ == "__main__": 
    s = DaySix() 
    print(f"Part 1: {s.task_one()}")
    print("WARNING: Part two takes ~3.5 mins (208 seconds) to run.\n"
      + "You may want to go get a coffee.")
    print(f"Part 2: {s.task_two()}")
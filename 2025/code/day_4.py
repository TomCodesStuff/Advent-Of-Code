from __future__ import annotations
from solution_base import Solution 


class PaperRoll(): 
    def __init__(self, coords) -> None:
        self.x, self.y = coords
        self.num_adjacents = 0
        self.neighbours = {} 
    

    def add_neighbour(self, coords : tuple[int, int], neighbour_roll : PaperRoll) -> None:
        if coords not in self.neighbours and neighbour_roll != self: 
            self.neighbours[coords] = neighbour_roll
            self.num_adjacents += 1
    

    def remove_neighbour(self, coords : tuple[int, int]) -> None:
        if coords in self.neighbours: 
            self.neighbours.pop(coords)
            self.num_adjacents -= 1


    def get_num_adjacents(self) -> int:
        return self.num_adjacents 


    def get_neighbours(self) -> dict[tuple[int, int], PaperRoll]: 
        return self.neighbours 


class DayFour(Solution): 


    def __init__(self) -> None:
        self.num_adjacent_rolls = 4


    def parse_puzzle_input(self) -> dict[tuple[int, int], PaperRoll]: 
        roll_grid = self.get_puzzle_input()
        
        coords_to_obj = {}
        for i in range(len(roll_grid)): 
            for j, grid_item  in enumerate(roll_grid[i]): 
                if grid_item == "@" and (j, i) not in coords_to_obj: 
                    coords_to_obj[(j, i)] = PaperRoll((j, i)) 
        
        for (x, y), paper_roll in coords_to_obj.items():  
            for i in range(max(0, y - 1), min(y + 2, len(roll_grid))): 
                for j in range(max(0, x - 1), min(x + 2, len(roll_grid[y]))): 
                    if (j, i) in coords_to_obj: 
                        paper_roll.add_neighbour((j, i), coords_to_obj[j, i])
                        coords_to_obj[j, i].add_neighbour((x, y), paper_roll)
        return coords_to_obj               

                    
    def task_one(self) -> int:
        total = 0
        for paper_roll in self.parse_puzzle_input().values(): 
            if paper_roll.get_num_adjacents() < self.num_adjacent_rolls: total += 1
        return total


    def task_two(self) -> int: 
        paper_roll_removed = True 
        total = 0 
        coords_to_obj = self.parse_puzzle_input()
        while(paper_roll_removed): 
            paper_roll_removed = False 
            for coords, paper_roll in list(coords_to_obj.items()):
                if paper_roll.get_num_adjacents() < self.num_adjacent_rolls: 
                    total += 1
                    paper_roll_removed = True
                    for neighbour in paper_roll.get_neighbours().values(): 
                        neighbour.remove_neighbour(coords) 
                    coords_to_obj.pop(coords)
        return total
                

if __name__ == "__main__": 
    s = DayFour() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
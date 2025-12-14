
import time 
import copy 
import os

DEFAULT_MAP = ["....#.....", 
             ".........#", 
             "..........", 
             "..#.......", 
             ".......#..", 
             "..........", 
             ".#..^.....", 
             "........#.", 
             "#.........", 
             "......#..."]   

OBSTRUCTION = "#"
COORD_TRANSFORMATIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)] 
GUARD_DIRECTIONS = ["^", ">", "v", "<"]
DIRECTIONS = ["Up", "Right", "Down", "Left"]
MAX_X = len(DEFAULT_MAP[0]) - 1
MAX_Y = len(DEFAULT_MAP) - 1


route_map = None
placeable_obstacles, loop_number = 0, 1
idx = 0


def print_map(task, num_positions, clear_flag=True):
    global placeable_obstacles, idx
     
    output = [f"\rTASK: {task}"]
    for row in route_map: output.append(row)
    output.append(f"Current Direction: {DIRECTIONS[idx]}")
    output.append(f"Distinct Positions: {num_positions}")
    if(task == 2): 
        output.append(f"Loop Number: {loop_number}")
        output.append(f"Placeable Obstructions: {placeable_obstacles}")
        sleep_time = 0.01
    else: sleep_time = 0.5 
    print(f"\033[{len(output)}A", end="")
    for j, line in enumerate(output):
        if("Current Direction" in line): 
            output[j] = f"Current Direction: {DIRECTIONS[idx]}"
        print("\033[K", end="") 
        print(output[j])
    time.sleep(sleep_time)


def get_start_position():  
    for i, line in enumerate(DEFAULT_MAP):
        for j, char in enumerate(line): 
            if char == "^": 
                return (j, i)


def create_copy():
    return copy.deepcopy(DEFAULT_MAP)


def apply_move(current_coords, direction):
    return tuple(x + y for x, y in zip(current_coords, direction))


def reverse_move(current_coords, direction):
    return tuple(x - y for x, y in zip(current_coords, direction))


def walk_route(task, start_coords):  
    global idx
    idx = 0
    route_visited = {start_coords: [COORD_TRANSFORMATIONS[idx]]}
    x, y = start_coords
    
    print_map(task, len(route_visited))
    while(True):
        route_map[y] = route_map[y][0:x] + "X" + route_map[y][x+1:]
        x, y = apply_move((x, y), COORD_TRANSFORMATIONS[idx])
        if(x < 0 or x > MAX_X): break 
        if(y < 0 or y > MAX_Y): break
        while(route_map[y][x] == OBSTRUCTION):
            x, y = reverse_move((x, y), COORD_TRANSFORMATIONS[idx])
            idx = (idx + 1) % 4 
            x, y = apply_move((x, y), COORD_TRANSFORMATIONS[idx])
        if((x, y) in route_visited):
            if COORD_TRANSFORMATIONS[idx] in route_visited[(x, y)]:
                return (route_visited, True) 
            route_visited[(x, y)].append(COORD_TRANSFORMATIONS[idx])
        else:
            route_visited[(x, y)] = [COORD_TRANSFORMATIONS[idx]]
        route_map[y] = route_map[y][0:x] + GUARD_DIRECTIONS[idx] + route_map[y][x+1:]
        print_map(task, len(route_visited))
    print_map(task, len(route_visited))
    return (route_visited, False)

        
def visualise_task_one(): 
    global route_map 
    route_map = create_copy()
    walk_route(1, get_start_position())
        

def visualise_task_two(): 
    start_pos = get_start_position()
    global route_map, placeable_obstacles, loop_number
    route_map = create_copy()
    distinct_route, _ = walk_route(2, start_pos) 
    del distinct_route[start_pos] 
    
    for x, y in distinct_route.keys():
        route_map = create_copy() 
        route_map[y] = route_map[y][0:x] + "#" + route_map[y][x+1:]
        route_visited, is_loop = walk_route(2, start_pos)
        if(is_loop): placeable_obstacles += 1    
        loop_number += 1
    print_map(2, len(route_visited), False)
        
os.system('cls' if os.name == 'nt' else 'clear')
visualise_task_one()
visualise_task_two()

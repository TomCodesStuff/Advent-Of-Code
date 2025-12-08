if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath  


def puzzle_input():
    puzzle_input = None 
    with open(getFilePath()) as f: 
        puzzle_input = f.read().splitlines() 
    return ((puzzle_input[0].find("S"), 0), puzzle_input)


def parse_tachyon_beams() -> int: 
    next_beams, found_beams = {}, {} 
    num_splits, timelines = 0, 0 
    starting_point, tachyon_manifold = puzzle_input()       
    found_beams[starting_point] = 1
    for row in tachyon_manifold:
        for beam, count in found_beams.items():   
            beam_x, beam_y = beam 
            beam_y += 1
            if(beam_y < len(tachyon_manifold)):  
                if row[beam_x] == "^": 
                    beam_left = (beam_x - 1, beam_y)
                    beam_right = (beam_x + 1, beam_y) 
                    if beam_left[0] >= 0:   
                        next_beams[beam_left] = next_beams.get(beam_left, 0) + count
                    if beam_right[0] < len(row):  
                        next_beams[beam_right] = next_beams.get(beam_right, 0) + count 
                    num_splits += 1
                else:   
                    next_beams[(beam_x, beam_y)] = next_beams.get((beam_x, beam_y), 0) + count            
        found_beams, next_beams = next_beams, {} 
        timelines = max(timelines, sum(found_beams.values())) 
    return num_splits, timelines


def task_one() -> int: 
    num_splits, _ = parse_tachyon_beams()
    return num_splits


def task_two() -> int:  
    _, timelines = parse_tachyon_beams()
    return timelines


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")
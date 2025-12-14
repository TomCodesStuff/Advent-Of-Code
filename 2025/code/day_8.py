import math
from solution_base.solution import Solution 


class DayEight(Solution):


    def __init__(self):
        self.num_shortest_connections = 1000


    def calculate_distance(self, a, b) -> float: 
        x1, y1, z1 = a
        x2, y2, z2 = b 
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2))


    def parse_puzzle_input(self):  
        puzzle_input = self.get_puzzle_input()
        coords = [tuple(int(x) for x in line.split(",")) for line in puzzle_input] 
        individual_coords = set()
        coords_by_distance = {}
        for i, coord_a in enumerate(coords):
            individual_coords.add(coord_a)
            for coord_b in coords[i+1:]: 
                coords_by_distance[(coord_a, coord_b)] = self.calculate_distance(coord_a, coord_b)  
        return ([k for k, _ in sorted(coords_by_distance.items(), key=lambda item: item[1])], len(individual_coords))
        

    def task_one(self) -> int: 
        coord_pairs, _ = self.parse_puzzle_input()
        circuits = [set([coord_pairs[0]])] 
        for coords_pair in coord_pairs[1:self.num_shortest_connections]:
            coord_a, coord_b = coords_pair
            circuits_to_merge = []
            for i, circuit in enumerate(circuits):  
                if coord_a in circuit or coord_b in circuit:  
                    circuits[i].add(coord_a)
                    circuits[i].add(coord_b) 
                    circuits_to_merge.append(circuits[i])
            if len(circuits_to_merge) == 0: circuits.append(set([coord_a, coord_b]))   
            elif len(circuits_to_merge) > 1:    
                merged_circuit = circuits_to_merge[0]
                circuits.remove(merged_circuit)
                for circuit in circuits_to_merge[1:]:
                    merged_circuit = merged_circuit.union(circuit)
                    circuits.remove(circuit) 
                circuits.append(merged_circuit) 
        
        circuits.sort(key=lambda x:len(x), reverse=True)
        return len(circuits[0]) * len(circuits[1]) * len(circuits[2])
        

    def task_two(self) -> int: 
        coord_pairs, num_coords = self.parse_puzzle_input()  
        circuits = [set([coord_pairs[0]])] 

        for pair in coord_pairs[1:]: 
            coord_a, coord_b = pair 
            circuits_to_merge = []
            for i, circuit in enumerate(circuits):  
                if coord_a in circuit or coord_b in circuit:
                    circuit.add(coord_a) 
                    circuit.add(coord_b) 
                    circuits_to_merge.append(i)

            if len(circuits_to_merge) == 0: circuits.append(set([coord_a, coord_b]))  
            elif len(circuits_to_merge) > 1: 
                merged_circuits = circuits[circuits_to_merge[0]]
                for circuit_idx in circuits_to_merge[1:]: 
                    merged_circuits = merged_circuits.union(circuits[circuit_idx])
                    circuits.remove(circuits[circuit_idx]) 
                circuits[circuits_to_merge[0]] = merged_circuits 
            
            for circuit in circuits: 
                if len(circuit) == num_coords: return coord_a[0] * coord_b[0]
        return 0

        
if __name__ == "__main__": 
    s = DayEight() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
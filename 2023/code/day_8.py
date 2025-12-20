import re
import math 
from solution_base import Solution 


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
        
   
class DayEight(Solution): 


    def create_network(self, puzzle_input):
        nodeDict =  {}
        startDict = {}
        for line in puzzle_input:
            nodes = re.sub(" =|[(),]", "", line.rstrip()).split(" ")
            if(nodes[0] not in nodeDict):
                nodeDict[nodes[0]] = Node(nodes[0])
                if(nodes[0][-1] == "A" and nodes[0] not in startDict):
                    startDict[nodes[0]] = nodeDict[nodes[0]]
            if(nodes[1] not in nodeDict): nodeDict[nodes[1]] = Node(nodes[1])
            if(nodes[2] not in nodeDict): nodeDict[nodes[2]] = Node(nodes[2])
            nodeDict[nodes[0]].left = nodeDict[nodes[1]]
            nodeDict[nodes[0]].right = nodeDict[nodes[2]]
        return startDict


    def traverse(self, instructions, startNode):
        currentNode = startNode
        i = 0
        n = len(instructions)
        steps = 0
        while(currentNode.val[-1] != "Z"):
            if(currentNode.left.val == currentNode.val and currentNode.right.val == currentNode.val): break 
            if(instructions[i] == "R"): currentNode = currentNode.right
            if(instructions[i] == "L"): currentNode = currentNode.left
            if(i == n - 1): i = 0
            else: i += 1
            steps += 1
        return steps


    def task_one(self):
        puzzle_input = self.get_puzzle_input()
        instructions = [c for c in puzzle_input[0]]
        startNode = self.create_network(puzzle_input[2:])
        return self.traverse(instructions, startNode["AAA"])


    def task_two(self):
        puzzle_input = self.get_puzzle_input()
        instructions = [c for c in puzzle_input[0]]
        nodes = self.create_network(puzzle_input[2:]) 

        nearestEnd = []
        for _, node in nodes.items(): nearestEnd.append(self.traverse(instructions, node))
        lcm = 1 
        for num in nearestEnd:
            lcm = math.lcm(lcm, num)
        return lcm


if __name__ == "__main__": 
    s = DayEight() 
    print(f"Part 1: {s.task_one()}")
    print(f"Part 2: {s.task_two()}")
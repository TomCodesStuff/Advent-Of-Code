import inspect 
import os
from abc import ABC, abstractmethod
from typing import Any


class Solution(ABC):
    def get_puzzle_input(self, puzzle_input_path : str|None = None) -> list[str]:
        if puzzle_input_path is None: 
            func_caller_path_parts = inspect.stack()[1].filename.split(os.sep) 
            puzzle_input_file = func_caller_path_parts[-1].replace(".py", ".txt") 
            # Using * to unpack func_caller_path_parts doesn't create correct path (on Windows)
            puzzle_input_path = os.path.join(os.sep.join(func_caller_path_parts[0:-2]), 
                                             "puzzle_inputs", puzzle_input_file) 

        with open(puzzle_input_path) as f: 
                return f.read().splitlines()


    @abstractmethod
    def task_one(self) -> Any: return


    @abstractmethod
    def task_two(self) -> Any: return
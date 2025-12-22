import importlib
import inspect
import os 
import random
import re 
import sys
from solution_base import Solution


SOLUTION_FILE_REGEX = "day_[0-9]{1,2}.py"


def print_available_commands(available_years : list[str]):
    print("\nType one of the commands below:")
    for year in available_years:
        print(f" - {year} -> Show available solutions for {year}.")  
    print(" - exit -> Exit the program.")
    print(" - help -> Output the list of available commands.")  
    print(" - song -> Recommend a random song that Tom likes.\n")  


def get_available_solutions(chosen_year : str) -> dict: 
    solutions_dir = os.path.join(chosen_year, "code")  
    return {file.split("_")[-1].replace(".py", "") : file.replace(".py", "") 
                           for file in os.listdir(solutions_dir) if re.match(SOLUTION_FILE_REGEX, file)} 


def print_available_solution_commands(chosen_year : str, available_solutions : dict) -> None:  
    first_day = min(available_solutions.keys(), key=int)
    last_day = max(available_solutions.keys(), key=int)

    print("\nType one of the commands below:")
    print(f" - <n> -> Run both solutions from the specified day in {chosen_year}.\n"
          f"          Available Days: {first_day} - {last_day}.")
    print(" - back -> Select a different year or command.")
    print(" - exit -> Exit the program.")
    print(" - help -> Output the list of available commands.\n") 


def import_solution(chosen_year : str, chosen_solution : str) -> Solution | None: 
    try:
        solution_module = importlib.import_module(f"{chosen_year}.code.{chosen_solution}")  
        for _, module_class in inspect.getmembers(solution_module, inspect.isclass): 
            if issubclass(module_class, Solution) and module_class is not Solution:   
                try:
                    return module_class()
                except Exception as ex:
                    print(f"ERROR: Solution Obj For Day {chosen_solution.split('_')[-1]} Could Not Be Instantiated.")
                    print(ex)
                    return None 
        print(f"ERROR: Solution Obj For Day {chosen_solution.split('_')[-1]} Could Not Be Found.")
        return None
    except ModuleNotFoundError as ex: 
        print(f"ERROR: No Module File Exists For Day {chosen_solution.split('_')[-1]}.")  
        print(ex)
        return None 
    

def print_array(arr : list[str]) -> None:  
    for row in arr: print("".join(row))
    print()

def run_solution(chosen_year : str, chosen_solution : str) -> Solution | None: 
    solution = import_solution(chosen_year, chosen_solution)
    if solution:
        print(f"\nDay {chosen_solution.split('_')[-1]} Of {chosen_year}:")
        task_one_result = solution.task_one() 
        if(isinstance(task_one_result, list)):  
            print("Task One: (See Below):")
            print_array(task_one_result)
        else: print(f"Task One: {task_one_result}")

        task_two_result = solution.task_two() 
        if(isinstance(task_two_result, list)): 
            print("Task Two: (See Below):")
            print_array(task_two_result)
        else: print(f"Task Two: {task_two_result}\n")


def choose_solution(chosen_year : str) -> None: 
    available_solutions = get_available_solutions(chosen_year)
    print_available_solution_commands(chosen_year, available_solutions)

    while(True):
        command_input = input(f"{chosen_year}: ").replace(" ", "").lower()
        if command_input == "exit": sys.exit(0)
        elif command_input in available_solutions: run_solution(chosen_year, available_solutions[command_input])
        elif command_input == "back": return 
    

def recommend_song():
    song = random.choice(open("songs.txt").read().splitlines())
    print(f"Tom recommends: {song}" ) 


def choose_command(available_years : list[str]):    
    print_available_commands(available_years)
    while(True):
        command_input = input("Command: ").replace(" ", "").lower()
        if command_input == "exit": sys.exit(0)
        elif command_input in available_years: choose_solution(command_input) 
        elif command_input == "help": print_available_commands(available_years)
        elif(command_input == "song"): recommend_song()


def main():
    print("Weclome to Tom's Advent of Code solutions!")
    availabe_years = [year for year in os.listdir("./") if year.isnumeric()]
    print("Available years: ", end="")
    for year in availabe_years[:-1]:
        print(f"{year}, ", end="")
    print(f"and {availabe_years[-1]}!")
    choose_command(availabe_years)


if(__name__ == "__main__"): main()
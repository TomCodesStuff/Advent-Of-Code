import os 
import importlib
import random
import re 
import sys


def main():
    print("Weclome to Tom's Advent of Code solutions!")
    availabe_years = [year for year in os.listdir("./") if year.isnumeric()]
    print("Available years: ", end="")
    for year in availabe_years[:-1]:
        print(f"{year}, ", end="")
    print(f"and {availabe_years[-1]}!")
    year_commands(availabe_years)


def print_available_commands(available_years : list[str]):
    print("Type one of the commands below:")
    for year in available_years:
        print(f" - {year} -> Show solutions for {year}.")  
    print(" - exit -> Exit the program.")
    print(" - help -> Output the list of available commands.")  
    print(" - song -> Recommend a random song that Tom likes.")  


def year_commands(available_years : list[str]):
    print_available_commands(available_years)
    
    while(True):
        command_input = input("Command: ").replace(" ", "") 
    #    if(commandInput in AOCYEARS): break
    #    elif(commandInput == "exit"): exit() 
     #   elif(commandInput == "song"): recommendSong()
     #   elif(commandInput == "help"): print_available_commands()
    #dayCommands(commandInput)


def getDayCommands(puzzleFiles): 
    dayToCommands = {}
    for file in puzzleFiles:
        dayNum = re.findall("[0-9]{1,2}",file)[0]
        dayCommand = "".join(re.split("day_|\\.py", file))
        if(int(dayNum) not in dayToCommands):
            dayToCommands[int(dayNum)] = [] 
        dayToCommands[int(dayNum)].append(dayCommand) 
    return dayToCommands


def printDayCommands(puzzleFiles):
    dayCommands = getDayCommands(puzzleFiles) 
    print(dayCommands)
    print("\nType one of the commands below:")
    for day in sorted(list(dayCommands.keys())): 
        for command in dayCommands[day]:
            if("CLI" in command): 
                print(f"\t - {command} -> Visualiser for day {day} (Test Data Only)")
            else: print(f"\t - {command} -> Solutions for day {day}")
    
    print("\t - back -> Return to year selection")
    print("\t - exit -> Close the program")
    print("\t - help -> Print a list of commands")


def dayCommands(year):
    puzzleFiles = [file for file in os.listdir(f"{DIRPATH}/{year}/code") 
                   if "day" in file]   
    
    printDayCommands(puzzleFiles)

    while(True):
        commandInput = input("Command: ").replace(" ", "") 
        if(f"day_{commandInput}.py" in puzzleFiles): outputDay(year, f"day_{commandInput}", commandInput)
        elif(commandInput == "back"): yearCommands()
        elif(commandInput == "exit"): exit()
        elif(commandInput == "help"): printDayCommands(puzzleFiles)


def outputDay(year, day, dayNumber):
    print(f"Solutions for Day {dayNumber}:")
    module_name = f"{year}.code.{day}"
    importlib.import_module(module_name)
    del sys.modules[module_name]


def recommendSong():
    song = random.choice(open("songs.txt").read().splitlines())
    print(f"Tom recommends: {song}" )


if(__name__ == "__main__"): main()
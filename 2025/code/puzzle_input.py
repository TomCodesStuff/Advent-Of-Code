import os
import inspect 

if(__name__ == "__main__"): 
     print("This file should be imported only.")
     exit()

def getFilePath():
     puzzleFile = inspect.stack()[1].filename.split(os.sep)[-1].split(".")[0] 
     dirs = os.getcwd().split(os.sep)
     if(dirs[-1] == "code"):
          return f"{os.sep.join(dirs[0:-1]) + os.sep}puzzle_inputs{os.sep}"+ puzzleFile +".txt"
     return os.getcwd() + f"{os.sep}puzzle_inputs{os.sep}"+ puzzleFile +".txt"
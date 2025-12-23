from datetime import datetime
from pathlib import Path 
from string import Template


class DayScaffold():  
    def __init__(self):
        self.number_to_word = {
            "1" : "One",  "2" : "Two",  "3" : "Three", "4" : "Four", "5" : "Five", 
            "6" : "Six", "7" : "Seven", "8" : "Eight", "9" : "Nine",  "10" : "Ten", 
            "11" : "Eleven", "12" : "Twelve", "13" : "Thirteen",  "14" : "Fourteen", "15" : "Fifteen", 
            "16" : "Sixteen", "17" : "Seventeen", "18" : "Eighteen", "19" : "Ninteen",  "20" : "Twenty", 
            "21" : "TwentyOne", "22" : "TwentyTwo", "23" : "TwentyThree", "24" : "TwentyFour", "25" : "TwentyFive"   
        }


    def build_day_scaffold(self, day:str="", year:str="") -> None:  
        if not year: year = datetime.today().strftime("%Y")
        if not day: day = datetime.today().strftime("%d")
        if day > "25": 
            print("SKIPPING: No puzzle as date exceeds the 25th.") 
            return 

        print(f"GENERATING: files for day {day} of {year}.")
        project_root = Path(__file__).parent.parent 

        # TODO both block similiar, can probably be made into a function
        py_file_path = project_root / year / "code" / f"day_{day}.py"
        if py_file_path.exists(): 
            print(f"SKIPPING: {py_file_path.name} exists in {py_file_path.parent}") 
        else:
            day_template_path = project_root / "templates" / "day_template.txt" 
            day_template = Template(day_template_path.read_text()).substitute({"day" : self.number_to_word[day]}) 
            try:  
                print(f"CREATING: `{py_file_path.name}` in `{py_file_path.parent}`.") 
                py_file_path.write_text(day_template)
            except FileNotFoundError:
                print(f"ERROR: `{py_file_path.name}` not created. One or more missing directories in `{py_file_path.parent}`.") 
         
        puzzle_input_path = project_root / year / "puzzle_inputs" / f"day_{day}.txt" 
        if puzzle_input_path.exists(): 
            print(f"SKIPPING: {puzzle_input_path.name} exists in {puzzle_input_path.parent}") 
            return 
        else:
            try: 
                print(f"CREATING: `{puzzle_input_path.name}` in `{puzzle_input_path.parent}`.") 
                puzzle_input_path.touch() 
            except FileExistsError: 
                print(f"ERROR: `{puzzle_input_path.name}` not created. One or more missing directories in `{puzzle_input_path.parent}`.") 


DayScaffold().build_day_scaffold(day="12", year="2025")
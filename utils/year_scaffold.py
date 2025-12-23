from datetime import datetime
from pathlib import Path
from string import Template


# TODO Add option to manually specify year 
class YearScaffold():
    

    def create_dir(self, dir_to_create : Path) -> None: 
        if dir_to_create.exists(): 
            print(f"SKIPPING: `{dir_to_create.name}` directory exists in `{dir_to_create.parent}`.")
        else:
            print(f"CREATING: `{dir_to_create.name}` directory in `{dir_to_create.parent}`.")
            dir_to_create.mkdir(exist_ok=True, parents=True)

    
    def generate_directory_structure(self) -> Path:  
        current_year = datetime.today().strftime("%Y")
        print(f"GENERATING: Directory structure for {current_year}.")
        project_root = Path(__file__).parent.parent 
        year_dir = project_root / current_year 
        self.create_dir(year_dir)
        self.create_dir(year_dir / "code")
        self.create_dir(year_dir / "puzzle_inputs")   
        return year_dir
    

    def generate_base_files(self, year_dir : Path) -> None: 
        print(f"GENERATING: Necessary base files.")
        init_path = year_dir / "code" / "__init__.py"
        if init_path.exists(): 
            print(f"SKIPPING: __init__.py exists in {year_dir / 'code'}")
        else: 
            print(f"CREATING: __init__.py in {str(year_dir / 'code')}") 
            init_path.touch()

       
        readme_template_path = year_dir.parent / "templates" / "README_template.txt"
        readme_path = year_dir / "README.md"
        if not readme_path.exists(): 
            print(f"CREATING: README.md in `{year_dir}`")
            readme_template = Template(readme_template_path.read_text()) 
            readme_path.write_text(readme_template.substitute({"year" : year_dir.name}))
        else:  
            print(f"SKIPPING: README.md exists in `{year_dir}`")


    def build_year_scaffold(self) -> None:
        year_dir = self.generate_directory_structure() 
        self.generate_base_files(year_dir) 


YearScaffold().build_year_scaffold()
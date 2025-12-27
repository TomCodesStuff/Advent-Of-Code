import json 
import os
import socket 
import ssl 
from datetime import datetime
from pathlib import Path


class PuzzleInputScraper(): 
    def __init__(self):
        self.first_aoc_year = 2015
        self.min_aoc_day = 1
        self.max_aoc_day = 25
        self.request_config = os.path.join("data", "request_config.json")
        self.buf_len = 4096 


    def load_request_config_data(self): 
        with open(Path(__file__).parent.parent / self.request_config) as f: 
            request_config_data = json.load(f)
        return (request_config_data["socket_data"], request_config_data["request_data"])


    def prepare_request(self, day : str, year : str) -> tuple[dict, bytes]: 
        socket_data, request_data = self.load_request_config_data()  
        session_cookie = os.getenv("SESSION_COOKIE")
        if session_cookie is None: 
            raise Exception(f"Required evironment variable SESSION_COOKIE is missing.") 
        else: request_data["headers"]["Cookie"] += session_cookie

        resource_path = f"/{year}/day/{day}/input"
        request = f"{request_data['method']} {resource_path} {request_data['protocol']}\r\n"
        
        for header, metadata in request_data["headers"].items(): 
            request += f"{header}: {metadata}\r\n"
        request += "\r\n" + request_data["body"]
        
        return (socket_data, request.encode("utf-8"))  
    

    def handle_request(self, socket_data : dict, request : bytes) -> str: 
        context = ssl.create_default_context() 
        sock = socket.create_connection((socket_data["host_url"], socket_data["port"]), 
                                        timeout=socket_data["timeout"]) 
        ssl_sock = context.wrap_socket(sock, server_hostname=socket_data["host_url"]) 
        ssl_sock.sendall(request)

        data = ""
        while data_chunk := ssl_sock.recv(self.buf_len):
            data += data_chunk.decode("utf-8")

        ssl_sock.close() 
        sock.close() 

        return data

    
    def parse_request_data(self, request_data : str) -> str:  
        request_data = request_data.replace("\r\n", "\n")
        puzzle_data = request_data.split("\n\n", 1)[1]
        return puzzle_data.strip()


    def cache_puzzle_input(self, puzzle_input : str, day : str, year : str) -> None: 
        project_root = Path(__file__).parent.parent 
        year_puzzle_input_dir = project_root / year / "puzzle_inputs" 
        if not year_puzzle_input_dir.exists(): text_file_path = project_root / f"day_{day}.txt" 
        else: text_file_path = year_puzzle_input_dir / f"day_{day}.txt" 

        with open(text_file_path, "w") as f: 
            f.write(puzzle_input)
    

    def scrape_puzzle_input(self, day:int=None, year:int=None) -> None:  
        latest_aoc_year = int(datetime.today().strftime("%Y"))
        current_month = int(datetime.today().strftime("%m"))
        if current_month != 12: latest_aoc_year -= 1

        if day is None: day = int(datetime.today().strftime("%d"))   
        if year is None: year = latest_aoc_year

        if day < self.min_aoc_day: 
            print("SKIPPING: No puzzle as date preceeds the 1st")
            return
        if day > self.max_aoc_day: 
            print("ERROR: No puzzle as date exceeds the 25th.")
            return 

        if not (self.first_aoc_year <= year <= latest_aoc_year):
            print(f"ERROR: {year} is an invalid year for Advent Of Code.\n"
                  f"Valid years are between {self.first_aoc_year} and {latest_aoc_year}.")
            return 
        

        socket_data, request = self.prepare_request(str(day), str(year))
        data = self.handle_request(socket_data, request)  
        puzzle_input = self.parse_request_data(data)
        self.cache_puzzle_input(puzzle_input, day, year)


PuzzleInputScraper().scrape_puzzle_input(day=1, year=2025)
# Advent Of Code: 

This repository contains my solutions for: 

- [Advent Of Code 2022](https://adventofcode.com/2022)
- [Advent Of Code 2023](https://adventofcode.com/2023) 
- [Advent Of Code 2024](https://adventofcode.com/2024) 
- [Advent Of Code 2025](https://adventofcode.com/2025)  

## 

| Year: | Last Completed Day: | Programming Language(s):|
| ----- | ------------------- | ----------------------- | 
|[2022](https://github.com/Thunder2103/Advent-Of-Code/tree/main/2022)  | Day 15              | Python                  |
|[2023](https://github.com/Thunder2103/Advent-Of-Code/tree/main/2023)  | Day 11              | Python                  |   
|[2024](https://github.com/Thunder2103/Advent-Of-Code/tree/main/2024)  | Day 11              | Python                  |  
|[2025](https://github.com/Thunder2103/Advent-Of-Code/tree/main/2025)  | Day 8               | Python                  |  

## Running Solutions: 

Each solution can be run from `main.py` (recommended). <br>
To run `main.py` simply input the following command in the project root. 

```bash 
python main.py 
```

Alternatively, solutions can be ran without using `main.py` by executing a version of the following command in the project root:

```bash
python -m year.code.day_x
``` 

Replacing `year` and `x` with the desired values. <br> 
For example:

```bash
python -m 2022.code.day_1
``` 

Would run the solutions for day one of 2022. 

## Automated Puzzle Input 

Puzzle inputs can be downloaded automatically from the website using the [`scrape_puzzle_input.py`](./utils/scrape_puzzle_input.py) script.

The automation script complies with the guidelines outlined in the [AOC reddit wiki.](https://www.reddit.com/r/adventofcode/wiki/faqs/automation/)<br> 
Specifically: 

- Outbound calls are throttled to every 15 minutes in `is_rate_limit_exceeded()`
- Downloaded inputs are cached in `cache_puzzle_input()`
- The User-Agent Header is defined in a JSON file located in `data/request_config.json` and is set to me (Tom) since I maintain this tool/repo. 

### Getting Your Puzzle Input

Downloading your unique puzzle inputs requires a [session cookie.](https://www.cookieyes.com/blog/session-cookies/)<br> 
To get your current session cookie follow the steps in [this video](https://www.youtube.com/watch?v=tUd33_CXCzE).

The script will expect the session cookie to be stored in an environment variable called `SESSION_COOKIE`. <br>
To create a environment variable copy-paste the following command into the terminal:

```bash 
export SESSION_COOKIE="session_cookie"
```
Make sure to replace `session_cookie` with your actual session cookie.
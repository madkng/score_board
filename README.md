# League Ranking Command-Line Application

This Python script processes match results from a league and outputs the team rankings based on specified rules. The solution is production-ready, maintainable, and testable.

## Problem statement
Create an application that can calculate the ranking table for a league

### Input/Output
The input an output will be text. Either using stdin/stdout or taking filenames on the command line is fine.

The input contains results of games, one per line.
The output should be ordered from most to least points, and if it is a draw, the names of the teams with the same amount of points, they must be sorted in alphabetical order.

### Scoring
In this league, a draw is worth 1 point and a win is worth 3 points. A loss is worth 0 points.

## Installation

- **Python 3.x** is required. Download it from [python.org](https://www.python.org/).
- No external dependencies are needed; the script uses only the standard library.

## Usage

### Running the Application
1. Save the input data in a text file (e.g., `input.txt`).
2. Run the script and redirect the input file:
   ```bash
   ./scoreboard.py < ./input/input.txt

3. You can also pipe the input file:
   ```bash
   cat input/sample_input.txt | ./scoreboard.py

#!/usr/bin/python3
"""
A module for tracking and displaying rankings in a league based on match results.

This module processes match results and generates rankings based on a points system where:
- Win = 3 points
- Draw = 1 point
- Loss = 0 points

Teams are ranked by total points (descending) and then alphabetically in case of ties.
"""
import sys
from collections import defaultdict

class League:
    """
    A class to manage league ranking based on match results.

    The class maintains team points and ranking, processing match results
    and generating ordered rankings based on points and team names.

    Attributes:
        team_points (defaultdict): Dictionary tracking points for each team
    """
    def __init__(self):
        """
        Constructor for League class
        """
        self.team_points = defaultdict(int)

    def process_match(self, line: str) -> None:
        """
        Process a single match result and update team points.

        Args:
            line (str): A string containing match result in the format
                       "Team1 Score1, Team2 Score2"

        Example:
            >>> league.process_match("Lions 3, Snakes 1")
        """
        team1_info, team2_info = line.strip().split(', ')
        team1_name, team1_score = team1_info.rsplit(' ', 1)
        team2_name, team2_score = team2_info.rsplit(' ', 1)

        score1, score2 = int(team1_score), int(team2_score)

        if score1 > score2:
            self.team_points[team1_name] += 3
            self.team_points[team2_name] += 0

        elif score2 > score1:
            self.team_points[team2_name] += 3
            self.team_points[team1_name] += 0

        else:
            self.team_points[team1_name] += 1
            self.team_points[team2_name] += 1

    def generate_ranking(self):
        """
        Calculate and return current league rankings.

        Returns:
            list: A list of tuples containing (rank, team_name, points),
                 sorted by points (descending) and then team name (alphabetically).
                 Teams with equal points receive the same rank.

        Example:
            >>> league.generate_ranking()
            [(1, "Lions", 6), (2, "Snakes", 3), (3, "Eagles", 0)]
        """


        #Take the team_points dictionary and sort it by points in descending order
        #If points are equal, sort by team name in ascending order
        sorted_teams = sorted(self.team_points.items(),
                            key=lambda x: (-x[1], x[0]))

        rankings = []
        curr_rank = 1
        prev_points = None

        for i, (team, points) in enumerate(sorted_teams):
            if points != prev_points:
                curr_rank = i + 1
                prev_points = points

            else:
                pass


            rankings.append((curr_rank, team, points))

        return rankings

    def format_ranking(self, ranking):
        """
        Print the current league rankings to standard output.

        Format: "Rank. Team Name, Points pts"
        Note: Uses "pt" for 1 point and "pts" for other values.

        Returns: A formatted string. See Example output
        >>> league.format_ranking(ranking)

        Example output:
            1. Lions, 6 pts
            2. Snakes, 3 pts
            3. Eagles, 0 pts
        """
        output = ""
        for rank, team, points in ranking:
            points_text = "pts" if points != 1 else "pt"
            output += f"{rank}. {team}, {points} {points_text}\n"


        return output.strip()

def process_input(input_lines):
    """
    Process multiple match results and return a populated Leuague object.

    Args:
        input_lines (list): List of strings containing match results,
                           one per line in the format "Team1 Score1, Team2 Score2"

    Returns:
        League: A League object containing processed match results

    Example:
        >>> lines = ["Lions 3, Snakes 1", "Eagles 1, Lions 1"]
        >>> league = process_input(lines)
    """
    league = League()
    for line in input_lines:
        if line.strip():
            league.process_match(line)
    return league

def main():
    """
    Main entry point for the script.

    Reads match results from standard input, processes them,
    and prints the final league rankings.

    Usage:
        $ python scoreboard.py < matches.txt
    """
    input_lines = sys.stdin.readlines()
    league = process_input(input_lines)
    ranking = league.generate_ranking()
    ranking = league.format_ranking(ranking=ranking)

    print(ranking)

if __name__ == "__main__":
    main()

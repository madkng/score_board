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

class LeagueRanking:
    """
    A class to manage league rankings based on match results.

    The class maintains team points and rankings, processing match results
    and generating ordered rankings based on points and team names.

    Attributes:
        team_points (defaultdict): Dictionary tracking points for each team
        teams_seen (set): Set of all teams that have participated in matches
    """
    def __init__(self):
        """
        Constructor for LeagueRanking class
        """
        self.team_points = defaultdict(int)
        self.teams_seen = set()

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

        self.teams_seen.add(team1_name)
        self.teams_seen.add(team2_name)

        score1, score2 = int(team1_score), int(team2_score)

        if score1 > score2:
            self.team_points[team1_name] += 3
        elif score2 > score1:
            self.team_points[team2_name] += 3
        else:
            self.team_points[team1_name] += 1
            self.team_points[team2_name] += 1

    def get_rankings(self):
        """
        Calculate current league rankings.

        Returns:
            list: A list of tuples containing (rank, team_name, points),
                 sorted by points (descending) and then team name (alphabetically).
                 Teams with equal points receive the same rank.

        Example:
            >>> league.get_rankings()
            [(1, "Lions", 6), (2, "Snakes", 3), (3, "Eagles", 0)]
        """
        if not self.teams_seen:
            return []

        for team in self.teams_seen:
            if team not in self.team_points:
                self.team_points[team] = 0

        sorted_teams = sorted(self.team_points.items(), 
                            key=lambda x: (-x[1], x[0]))

        rankings = []
        curr_rank = 1
        prev_points = None
        same_rank_count = 0

        for i, (team, points) in enumerate(sorted_teams):
            if points != prev_points:
                curr_rank = i + 1
                prev_points = points
                same_rank_count = 1
            else:
                same_rank_count += 1
            rankings.append((curr_rank, team, points))

        return rankings

    def print_rankings(self):
        """
        Print the current league rankings to standard output.

        Format: "Rank. Team Name, Points pts"
        Note: Uses "pt" for 1 point and "pts" for other values.

        Example output:
            1. Lions, 6 pts
            2. Snakes, 3 pts
            3. Eagles, 0 pts
        """
        for rank, team, points in self.get_rankings():
            points_text = "pts" if points != 1 else "pt"
            print(f"{rank}. {team}, {points} {points_text}")

def process_input(input_lines):
    """
    Process multiple match results and return a populated LeagueRanking object.

    Args:
        input_lines (list): List of strings containing match results,
                           one per line in the format "Team1 Score1, Team2 Score2"

    Returns:
        LeagueRanking: A LeagueRanking object containing processed match results

    Example:
        >>> lines = ["Lions 3, Snakes 1", "Eagles 1, Lions 1"]
        >>> league = process_input(lines)
    """
    league = LeagueRanking()
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
    league.print_rankings()

if __name__ == "__main__":
    main()

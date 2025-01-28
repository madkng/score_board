import sys
from collections import defaultdict

class LeagueRanking:
    def __init__(self):
        self.team_points = defaultdict(int)
        self.teams_seen = set()
        
    def process_match(self, line: str) -> None:
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
        for rank, team, points in self.get_rankings():
            points_text = "pts" if points != 1 else "pt"
            print(f"{rank}. {team}, {points} {points_text}")

def process_input(input_lines):
    league = LeagueRanking()
    for line in input_lines:
        if line.strip():
            league.process_match(line)
    return league

def main():
    input_lines = sys.stdin.readlines()
    league = process_input(input_lines)
    league.print_rankings()

if __name__ == "__main__":
    main()
import unittest
from io import StringIO
import sys
from scoreboard import LeagueRanking, process_input

class TestLeagueRanking(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def run_test(self, input_lines, expected_output):
        captured_output = StringIO()
        sys.stdout = captured_output
        league = process_input(input_lines)
        league.print_rankings()
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue().strip().split('\n') if captured_output.getvalue().strip() else []
        self.assertEqual(actual_output, expected_output)

    def test_original_sample(self):
        input_lines = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0"
        ]
        expected_output = [
            "1. Tarantulas, 6 pts",
            "2. Lions, 5 pts",
            "3. FC Awesome, 1 pt",
            "3. Snakes, 1 pt",
            "5. Grouches, 0 pts"
        ]
        self.run_test(input_lines, expected_output)

    def test_all_teams_zero_points(self):
        input_lines = [
            "Team A 0, Team B 0",
            "Team C 0, Team D 0"
        ]
        expected_output = [
            "1. Team A, 1 pt",
            "1. Team B, 1 pt",
            "1. Team C, 1 pt",
            "1. Team D, 1 pt"
        ]
        self.run_test(input_lines, expected_output)

    def test_multiple_ties_different_points(self):
        input_lines = [
            "Arsenal 3, Chelsea 0",     # Arsenal 3, Chelsea 0
            "Liverpool 3, ManCity 0",   # Liverpool 3, ManCity 0
            "Arsenal 0, Liverpool 0",   # Arsenal 4, Liverpool 4
            "Chelsea 3, ManCity 0",     # Chelsea 3, ManCity 0
            "Spurs 1, Leeds 1"         # Spurs 1, Leeds 1
        ]
        expected_output = [
            "1. Arsenal, 4 pts",
            "1. Liverpool, 4 pts",
            "3. Chelsea, 3 pts",
            "4. Leeds, 1 pt",
            "4. Spurs, 1 pt",
            "6. ManCity, 0 pts"
        ]
        self.run_test(input_lines, expected_output)

    def test_single_team_all_wins(self):
        input_lines = [
            "Winner 1, TeamA 0",
            "Winner 2, TeamB 0",
            "Winner 3, TeamC 0"
        ]
        expected_output = [
            "1. Winner, 9 pts",
            "2. TeamA, 0 pts",
            "2. TeamB, 0 pts",
            "2. TeamC, 0 pts"
        ]
        self.run_test(input_lines, expected_output)

    def test_empty_input(self):
        self.run_test([], [])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            process_input(["Invalid Input"])
        with self.assertRaises(ValueError):
            process_input(["Team A 1, Team B"])
        with self.assertRaises(ValueError):
            process_input(["Team A, Team B 1"])

if __name__ == '__main__':
    unittest.main()
import unittest
from io import StringIO
import sys
from scoreboard import LeagueRanking, process_input

class TestLeagueRanking(unittest.TestCase):
    def test_sample_input(self):
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
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        league = process_input(input_lines)
        league.print_rankings()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        actual_output = captured_output.getvalue().strip().split('\n')
        self.assertEqual(actual_output, expected_output)
        
    def test_empty_input(self):
        league = process_input([])
        self.assertEqual(league.get_rankings(), [])
        
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            process_input(["Invalid Input"])
            
    def test_tie_alphabetical_order(self):
        input_lines = [
            "Team B 1, Team C 1",
            "Team A 1, Team D 1"
        ]
        league = process_input(input_lines)
        rankings = league.get_rankings()
        
        # All teams should have same rank and be in alphabetical order
        self.assertEqual(rankings[0], (1, "Team A", 1))
        self.assertEqual(rankings[1], (1, "Team B", 1))
        self.assertEqual(rankings[2], (1, "Team C", 1))
        self.assertEqual(rankings[3], (1, "Team D", 1))

if __name__ == '__main__':
    unittest.main()
import unittest
from src.scoreboard import League

class TestLeague(unittest.TestCase):

    def test_process_match(self):
        inp = "Lions 3, Snakes 3"
        expected = {"Lions": 1, "Snakes":1}

        league = League()
        league.process_match(inp)

        self.assertEqual(league.team_points, expected)

    def test_generate_ranking(self):
        expected = [(1, "Tarantulas", 6),
                    (2, "Lions", 5),
                    (3, "FC Awesome", 1),
                    (3, "Snakes", 1),
                    (5, "Grouches", 0)]

        league = League()
        league.team_points = {"Tarantulas" : 6, "Lions": 5, "FC Awesome": 1,
                              "Snakes" : 1, "Grouches" : 0}

        actual = league.generate_ranking()

        self.assertEqual(actual, expected)

    def test_get_ranking(self):
        expected = """1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts"""
        inp = [(1, "Tarantulas", 6),
                    (2, "Lions", 5),
                    (3, "FC Awesome", 1),
                    (3, "Snakes", 1),
                    (5, "Grouches", 0)]

        league = League()
        actual = league.format_ranking(inp)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    """
    Run unit tests
    """
    unittest.main()
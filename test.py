#! /usr/bin/python
import unittest
from solution import *

class MatchResultMock(object):
    def __init__(self, teams, scores):
        self.teams = teams
        self.scores = scores

class TestMatchResult(unittest.TestCase):
    def test___init__(self):
        """Test that we correctly parse result input lines"""
        m = MatchResult(""" team A with spaces 1, Snakes 3
""")
        self.assertTupleEqual(m.teams, ('team A with spaces', 'Snakes'))
        self.assertTupleEqual(m.scores, (1, 3))

class TestTable(unittest.TestCase):
    def test_record_result(self):
        """Test that table dictionary is updated with correct teams and points.
        3 points for a win, 0 for loss, 1 for tie."""
        t = Table()
        # test tie
        t.record_result(MatchResultMock(('a', 'b'), (0, 0)))
        self.assertDictEqual({'a': 1, 'b': 1}, t.teams)
        # test loss for existing team, win for new team
        t.record_result(MatchResultMock(('a', 'c'), (50, 100)))
        self.assertDictEqual({'a': 1, 'b': 1, 'c': 3}, t.teams)
        # test win for existing team, loss for new team
        t.record_result(MatchResultMock(('a', 'd'), (4, 0)))
        self.assertDictEqual({'a': 4, 'b': 1, 'c': 3, 'd': 0}, t.teams)
    
    def Convert(self):
        """Test that _rank_comparison correctly sorts by points and alphabet."""
        t = Table()
        t.tuple = [('a',2),('cx',3),('df',3)]
        dictionary = {}
        teams = t.Convert(t.tuple,dictionary)
        self.assertEqual(sorted(teams,  key=lambda a: (-a[1], a[0])),{'cx':3,'df':3,'a':2})

    def test_generate_rankings(self):
        """Test that our ranking output lines are generated and formatted correctly"""
        input = """Crazy Ones 3, Rebels 3
Fantastics 1, FC Super 0
Crazy Ones 1, FC Super 1
Fantastics 3, Rebels 1
Crazy Ones 4, Misfits 0"""
        expected_output = """1. Fantastics, 6 pts
2. Crazy Ones, 5 pts
3. FC Super, 1 pt
3. Rebels, 1 pt
5. Misfits, 0 pts
"""
        t = Table()
        for line in input.splitlines(True):
            t.record_result(MatchResult(line))
        output = ""
        for line in t.generate_rankings():
            output += line + "\n"
        self.assertMultiLineEqual(expected_output, output)
        
if __name__ == '__main__':
    unittest.main()
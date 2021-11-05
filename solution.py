#! /usr/bin/python
import argparse
import fileinput
import re
import sys

class MatchResult(object):
    """Soccer match result."""
    def __init__(self, line):
        """Parse a match result string into teams and scores."""
        self.teams = ()
        self.scores = ()
        for teamResult in line.split(','):
            self.teams += re.search("(\S+.*?)\s+\d+\s*$", teamResult).group(1),
            self.scores += int(re.search("(\d+)\s*$", teamResult).group(1)),

class Table():
    """Soccer league table."""
    def _record_win(self, team):
        self.teams[team] += 3

    def _record_tie(self, team):
        self.teams[team] += 1

    def __init__(self):
        self.teams = {}
    
    def record_result(self, result):
        """Update the table's teams and their points based on a match result."""
        for name in result.teams:
            if name not in self.teams:
                self.teams[name] = 0
        team1, team2 = result.teams
        score1, score2 = result.scores 
        if score1 == score2:
            self._record_tie(team1)
            self._record_tie(team2)
        else:
            self._record_win(team1 if score1 > score2 else team2)

    """ Converter for tuple into dictionary"""
    def Convert(self, tup, di):
        di = dict(tup)
        return di

    def generate_rankings(self):
        """Generate ordered ranking strings of teams and their points in the table."""
        lastPoints = 0
        rank = 1
        dict = self.teams
        list = [(k, v) for k, v in dict.items()]
        record = sorted(list, key=lambda a: (-a[1], a[0])) #Sorting by points, or by team name if points are tied.
        dictionary = {}
        teams = self.Convert(record, dictionary) 
        for index, team in enumerate(teams, start=1):
            points = teams[team]
            if points != lastPoints:
                rank = index
            points_string = "pt" if points == 1 else "pts"
            yield "%d. %s, %d %s" % (rank, team, points, points_string)
            lastPoints = points            

    def print_rankings(self):
        """Print descending ranking of teams and their points in the table."""
        for line in self.generate_rankings():
            print (line)

def get_input():
    """Do arg parsing. Return generator for input lines."""
    parser = argparse.ArgumentParser(description='Output the ranking table for a soccer league.')
    parser.add_argument(
        'file', nargs='?', help=(
            "File containing match results. If not specified, "
            "the same format is expected via standard input pipe. "
            "See README.md for format details."
        ))
    args = parser.parse_args()
    if args.file:
        def lineGenerator():
            with open(args.file) as f:
                for line in f:
                    yield line
        return lineGenerator()
    elif not sys.stdin.isatty():
        return (line for line in fileinput.input())
    else:
        parser.print_help()
        exit()

def main():
    table = Table()
    for line in get_input():
        table.record_result(MatchResult(line))  
    table.print_rankings()

if __name__ == "__main__":
    main() 
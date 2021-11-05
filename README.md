This is a small program/task which demonstrates some python code. It is a command-line application that will calculate the ranking table for a sport league given some match results.

The main program is solutions.py

Command line help is available with no arguments and no standard input, or an argument of -h or --help

The main program (see solution.py) can be run by executing command: python solution.py sample-input.txt or python3 solution.py sample-input.txt 

The input is game results, one per line (see sample-input.txt). The output is a ranking of teams and their points, one per line (see expected-output.txt). We expect that the input will be well-formed.

In this league, teams accumulate points by winning (3 points) or drawing (1 point) or loss (0 points). If two teams have the same number of points, they are ranked equally and are output in alphabetical order.

Tests are in test.py and can be run by executing test.py. The tests assume solution.py is in the same directory or in the module path.

Tests can be run by executing command:python -m test or python3 -m test and also using command: python test.py or command: python3.test.py.

tigerlab is named of my Virtual Environments of python3 and can create a virtual environment by executing command: python3 -m venv tigerlab.

Active by using command: tigerlab\Scripts\activate on Window. And On Unix or MacOS, run: source tigerlab/bin/activate.To deactivate this virtual environments using command: source tigerlab/bin/deactivate on command-line interface (cmd) or on power shell by running command: deactivate. 

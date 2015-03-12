import sys, os, datetime

if __name__ == "__main__":

    problem_name = 'problem'
    probs_path = os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0], 'problems')
    i = [int(i.split('_')[-1]) for i in os.listdir(probs_path) if i.split('_')[0] == problem_name]
    highest_prob_attempted = max(i) if i else 0
    next_prob_num = highest_prob_attempted + 1
    new_prob_dir = os.path.join(probs_path, '{problem_name}_{problem_number}'.format(problem_name=problem_name, problem_number=next_prob_num))
    os.mkdir(new_prob_dir)
    with open(os.path.join(new_prob_dir, 'script.py'), 'w') as f:
        f.writelines(
"""#
# Problem {prob_num} of Project Euler (https://projecteuler.net/problem={prob_num})
#
# Attempted by Rich Lewis on {date}
#

from __future__ import print_function

def solution():
    return 42

if __name__ == "__main__":
    print("solution: ", solution())""".format(prob_num=next_prob_num, date=datetime.date.today()))

    with open(os.path.join(new_prob_dir, 'test_script.py'), 'w') as f:
        f.writelines(
"""#
# Tests for Problem {prob_num} of Project Euler (https://projecteuler.net/problem={prob_num})
#
# Rich Lewis on {date}
#

from .script import solution

class TestSolution(object):
    def test_sol(self):
        assert solution() == 42""".format(prob_num=next_prob_num, date=datetime.date.today()))

    with open(os.path.join(new_prob_dir, '__init__.py'), 'w') as f:
        pass

    os.chdir(new_prob_dir)

#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = []
    if n < 0:
        return []
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]

    def helper(n, plays):
        if n < 0:
            return []
        if n == 1:
            return [['rock'], ['paper'], ['scissors']]
        curr_plays = []
        rock_options = [['rock', 'rock'], [
            'rock', 'paper'], ['rock', 'scissors']]
        paper_options = [['paper', 'paper'], [
            'paper', 'scissors'], ['paper', 'rock']]
        scissors_options = [['scissors', 'scissors'], [
            'scissors', 'paper'], ['scissors', 'rock']]
        curr_plays = curr_plays + [rock_options[n]] + \
            [paper_options[n]] + [scissors_options[n]]
        # if n == 0:
        return plays + curr_plays
        # return plays + curr_plays + helper(n-1, plays) + helper(n-2,plays)
    return helper(n, plays) + helper(n-1, plays) + helper(n-2, plays)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

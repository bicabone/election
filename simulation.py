from csv_utils import *
from stat_utils import *
import enum


class Party(enum.Enum):
    RED = 1
    BLUE = 2
    COMMUNIST = 3


class Simulation:

    def __init__(self) -> None:
        super().__init__()
        self.stdevs = read_stdev()
        self.avgs = read_avg()
        self.electoral = read_electoral_to_dict()
        self.states = self.electoral.keys()
        self.labels = {
            "Donald Trump": Party.RED,
            "Joseph R. Biden Jr.": Party.BLUE,
            "Convention Bounce for Donald Trump": Party.RED,
            "Convention Bounce for Joseph R. Biden Jr.": Party.BLUE
        }
        self.opponents = {
            Party.RED: Party.BLUE,
            Party.BLUE: Party.RED
        }

    def count(self, state, label):
        mean = self.avgs[state][label]["avg"]
        stdev = self.stdevs[state][label]["stdev"]
        prob = sample_normal(mean, stdev)
        winner = coin_flip(prob)
        party = self.labels[label]
        electoral_votes = self.electoral[state]
        if winner:
            return party, electoral_votes
        else:
            return self.opponents[party], electoral_votes

    def run(self, label):
        red = 0
        blue = 0

        for state in self.states:
            party, votes = self.count(state, label)
            if party == Party.RED:
                red += votes
            elif party == Party.BLUE:
                blue += votes

        assert red + blue == 538

        if red >= 270:
            return Party.RED
        elif blue >= 270:
            return Party.BLUE
        else:
            return Party.COMMUNIST

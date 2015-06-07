# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Description: For every agent that enters the model, match them to a house that satisfies their requirements
# Created on: 6/6/15
# Created by: Jean-Ezra Yeung

# Outline
# 1. Objects - Generate 2 lists: renters, houses
# 2. Emergence - Match renters and houses based on price and niceness (quality for acceptance)
# 3. Complexity

# Agent flow:
# 1. Cohort of agents enters a market with a set of houses
# 2. Agents choose a house of interest
#     2a. Whoever loops first gets the house
# 3. Agents re-bid based on new market



import pandas as pd
from pandas import Series, DataFrame



# 1. Objects - Generate 2 lists: renters, houses
class Renters:
    def __init__(self, cohort, match_score, demand):
        self.cohort = 1
        self.features = list(DataFrame(np.random.randint(match_score, size= (demand,1)))[0])

class Houses:
    def __init__(self, cohort, match_score, supply):
        self.cohort = 1
        self.features = list((DataFrame(np.random.randint(match_score, size= (supply,1))))[0])



# 2. Emergence - Match renters and houses based on a set of features

def match(time,match_score,demand,supply):
    r = Renters(cohort,match_score,demand)
    h = Houses(cohort,match_score,supply)
    renter = r.features
    print renter
    house = h.features
    print house
    match_r = []
    match_h = []
    no_match_r = []
    no_match_h = []
    for t in time:
        for i in renter:
            for j in house:
                if i == j:
                    match_r.append(i)
                    match_h.append(j)
                elif i != j:
                    no_match_r.append(i)
                    no_match_h.append(j)
        print 'Cycle:', t
        print 'Renter match:', '\n', 'renter |', 'matches', '\n', match_r, '\n', (Series(match_r)).value_counts(ascending=True)
        print 'House match:', '\n', 'house |', 'matches', '\n', match_h, '\n', (Series(match_h)).value_counts(ascending=True)
        print 'No renter match:', '\n', 'renter |', 'no matches', '\n', no_match_r, '\n', (Series(no_match_r)).value_counts(ascending=True)
        print 'No house match:', '\n', 'house |', 'no matches', '\n', no_match_h, '\n', (Series(no_match_h)).value_counts(ascending=True)
        # Add new renters and houses for each cycle
#         renters.append(range(11,20))
#         houses.append(range(11,20))

# if __name__ == "__main__":
# Parameters
time = list(range(1,2))
cohort = 'A'
match_score = 10
demand = 11
supply = 11
# Run
match(time,match_score,demand,supply)

import classes
import random
import math
import numpy as np
import house_match as h
import csv


def generate_renters(n=1000, min_scores=[1, 2, 3, 4, 5]):
    '''
    Generates renters based on 2013 distribution of San Francisco household
    incomes assuming each household can spend a max of 1/3 of pretax income
    on rent.
    inputs: n is number of renters, min_scores is the distribution of minimum
    housing scores that renters will accept
    '''
    avg_income = 80000
    sigma = .98  # sigma needed so 5% households above 423k (1.645 st dev)
    renters = []
    for i in xrange(n):
        min_score = random.choice(min_scores)
        income = int(np.random.lognormal(mean=math.log(avg_income),
                                         sigma=sigma))
        renters.append(classes.Renter(income/36, min_score))
    return renters


def generate_houses(house_scores={1: 150, 2: 200, 3: 250, 4: 200, 5: 150}):
    '''
    input the number houses of each score as a dictionary
    '''
    houses = []
    for score, num in house_scores.iteritems():
        houses += [classes.House(score) for h in xrange(num)]
    return houses


def simulate(num_renters=1500,
             house_scores={1: 150, 2: 200, 3: 250, 4: 200, 5: 150},
             filename='output.csv'):
    '''
    runs simulation and outputs results as csv files
    '''
    f = open(filename, 'w')
    fieldnames = ['min_score', 'max_rent', 'rent', 'apt_score']
    dw = csv.DictWriter(f, fieldnames)
    dw.writeheader()
    houses = generate_houses(house_scores)
    renters = generate_renters(num_renters)
    h.stable_match(renters, houses)
    for renter in sorted(renters, key=lambda x: x.willingness_to_pay):
        dic = {'max_rent': renter.willingness_to_pay,
               'min_score': renter.min_score, 'rent': renter.paying,
               'apt_score': (renter.renting.score if renter.matched else None)}
        # print dic
        dw.writerow(dic)
    f.close()
    # print np.mean([r.paying for r in renters if r.matched])
    # print np.median([r.paying for r in renters if r.matched])


def run_simulation():
    '''
    runs simulator 3 times with 15,000 renters first with 10k houses with a
    somewhat normal distribution of the 5 housing scores, then with
    2k (luxury) score 5 houses added for a total of 12k houses, then with
    12k houses with lower score houses added.
    '''
    renters = 15000
    houses = {1: 1500, 2: 2000, 3: 2500, 4: 2000, 5: 1500}
    simulate(num_renters=renters, house_scores=houses, filename='normal.csv')
    houses[5] += 2000  # simulating with more luxury apartments
    simulate(num_renters=renters, house_scores=houses, filename='luxury.csv')
    houses = {1: 2000, 2: 2500, 3: 2500, 4: 2000, 5: 1500}
    simulate(num_renters=renters, house_scores=houses, filename='cheap.csv')


if __name__ == '__main__':
    run_simulation()

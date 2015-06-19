import classes
import math
import numpy as np
import random


def generate_renters(renter_min_scores):
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
    for min_score, num in renter_min_scores.iteritems():
        for i in xrange(num):
            income = int(np.random.lognormal(mean=math.log(avg_income),
                                             sigma=sigma))
            renters.append(classes.Renter(income/36, min_score))
    random.shuffle(renters)
    return renters


def generate_houses(house_scores):
    '''
    input the number houses of each score as a dictionary
    '''
    houses = []
    for score, num in house_scores.iteritems():
        houses += [classes.House(score) for h in xrange(num)]
    return houses
import classes
reload(classes)
import random
import math
import numpy as np

min_standard_dist = [.2, .3, .3, .1, .1]
niceness_dist = [.15, .3, .25, .15, .15]


annual_growth = (852469./805195)**(12./51)
# annualized growth from April 2010 to July 2014


def renters(n=100):
	avg_income = 80000
	sigma = .978 # sigma needed so 5% households above 423k (1.645 st dev)

	renters = []
	for i in xrange(n):
		income = int(np.random.lognormal(mean=math.log(avg_income),sigma=sigma))
		renters.append(classes.Renter(income/36,i))
	return renters



import classes
reload(classes)
import random

min_standard_dist = [.2, .3, .3, .1, .1]
niceness_dist = [.15, .3, .25, .15, .15]


def renters(n=100):
	renters = []
	for i in xrange(n):
		standard = random.choice([0,1,2,3,4])
		rooms = random.choice([1,2])
		rent = int(abs(random.gauss(1000*rooms + 500* standard, 600 + 300 * standard)))
		renters.append(classes.Renter(i, rent, standard, rooms))
	return renters



import classes
import random
import math
import numpy as np
import house_match as h


def generate_renters(n=300):
	avg_income = 80000
	sigma = .98 # sigma needed so 5% households above 423k (1.645 st dev)
	renters = []
	for i in xrange(n):
		income = int(np.random.lognormal(mean=math.log(avg_income),sigma=sigma))
		renters.append(classes.Renter(income/36,i))
	return renters	

def generate_houses(n=200):
	return [classes.House(random.randint(1,10)) for h in xrange(n)]

def test():
	'''
	runs simulation with 300 renters with variety of number of houses
	'''
	for n in [300, 250, 200, 150]:
		houses = generate_houses(n)
		renters = generate_renters(300)
		h.stable_match(renters, houses)
		for renter in sorted(renters, key=lambda x: x.willingness_to_pay):
			print renter.willingness_to_pay, renter.paying, renter.matched, (
				renter.renting.niceness if renter.matched else None)
		print np.mean([r.paying for r in renters if r.matched])
		print np.median([r.paying for r in renters if r.matched])

def time(n=500, growth=.1):
	'''
	currently doesn't work. want to simulate population growth and 30%
	leaving apartment every year

	'''
	houses = generate_houses(n-100)
	renters = generate_renters(n)
	for z in xrange(10):
		h.stable_match(renters, houses)
		for house in random.sample(houses, int(n*.3)):
			print house.occupied
			house.rented_by.set_matched(None,False)
			house.occupied = False
			house.rented_by = None
		for renter in sorted(renters, key=lambda x: x.willingness_to_pay, reverse=True):
			print renter.willingness_to_pay, renter.paying, renter.matched, (renter.renting.niceness if renter.matched else None)
		renters += generate_renters(int(n*growth))
		print np.mean([r.paying for r in renters if r.matched])
		print np.median([r.paying for r in renters if r.matched])
		print len(renters)

if __name__ == '__main__':
	test()

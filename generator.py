import classes
import random
import math
import numpy as np
import house_match as h
import csv


def generate_renters(n=1000, dist=[1, 2, 3, 4, 5]):
	avg_income = 80000
	sigma = .98 # sigma needed so 5% households above 423k (1.645 st dev)
	renters = []
	for i in xrange(n):
		min_score = random.choice(dist)
		income = int(np.random.lognormal(mean=math.log(avg_income),sigma=sigma))
		renters.append(classes.Renter(income/36,min_score))
	return renters	

def generate_houses(dist={1:150, 2:200, 3:250, 4:200, 5:150}):
	houses = []
	for score, num in dist.iteritems():
		houses += [classes.House(score) for h in xrange(num)]
	return houses

def simulator(num_renters=1500, house_dist={1:150, 2:200, 3:250, 4:200, 5:150}, filename='output.csv'):
	'''
	runs simulation with 300 renters with variety of number of houses
	'''
	f = open(filename,'w')
	fieldnames = ['min_score', 'max_rent', 'rent', 'apt_score']
	dw = csv.DictWriter(f, fieldnames)
	dw.writeheader()
	houses = generate_houses(house_dist)
	renters = generate_renters(num_renters)
	h.stable_match(renters, houses)
	for renter in sorted(renters, key=lambda x: x.willingness_to_pay):
		dic = {'max_rent': renter.willingness_to_pay, 'min_score': renter.min_score, 
			  'rent': renter.paying, 'apt_score': (renter.renting.score if renter.matched else None)}
		dw.writerow(dic)
	f.close()
		# print dic
	# print np.mean([r.paying for r in renters if r.matched])
	# print np.median([r.paying for r in renters if r.matched])

def test():
	simulator(num_renters=15000, house_dist={1:1500, 2:2000, 3:2500, 4:2000, 5:1500}, filename='regular.csv')
	simulator(num_renters=15000, house_dist={1:1500, 2:2000, 3:2500, 4:2000, 5:3500}, filename='more_luxury.csv')
	simulator(num_renters=15000, house_dist={1:2500, 2:3000, 3:2500, 4:2000, 5:1500}, filename='more_cheap.csv')


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
			print renter.willingness_to_pay, renter.paying, renter.matched, (renter.renting.score if renter.matched else None)
		renters += generate_renters(int(n*growth))
		print np.mean([r.paying for r in renters if r.matched])
		print np.median([r.paying for r in renters if r.matched])
		print len(renters)

if __name__ == '__main__':
	test()

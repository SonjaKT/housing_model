import scipy.stats
import numpy.random
import classes
import house_match

def create_renters(n_renters, scaling_factor = 1000):
	renter_list = []
	rvs = scipy.stats.chi2.rvs(df = 4, size=n_renters)
	for index, r in enumerate(rvs):
		renter_list.append(classes.Renter(r*scaling_factor, index))
	return renter_list
	
def create_houses(n_houses, mean_quality = 100, sd = 10):
	house_list = []
	samples = numpy.random.normal(mean_quality, sd, n_houses)
	for index, sample in enumerate(samples):
		house_list.append(classes.House(sample))
	return house_list

renters = create_renters(50)
houses = create_houses(30)

houses.extend(create_houses(10, 120, 10))
renters.extend(create_renters(5, 1500))

houses = house_match.sort_houses_by_niceness(houses)

house_match.stable_match(renters, houses)

for house in houses:
        print house.niceness, renters[house.rented_by].willingness_to_pay, renters[house.rented_by].paying




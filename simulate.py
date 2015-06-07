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

def simulation(n_renters, n_houses, higher_quality_houses = 0, lower_quality_houses = 0):

	renters = create_renters(n_renters)
	houses = create_houses(n_houses)

	if higher_quality_houses:
		houses.extend(create_houses(higher_quality_houses, 120, 10))
		renters.extend(create_renters(higher_quality_houses / 2, 1500))

	if lower_quality_houses:
		houses.extend(create_houses(lower_quality_houses, 80, 10))
		renters.extend(create_renters(lower_quality_houses / 2, 500))

	houses = house_match.sort_houses_by_niceness(houses)

	house_match.stable_match(renters, houses)

	#do stats
	max_price = renters[houses[0].rented_by].paying
	median_price = renters[houses[len(renters)/2].rented_by].paying

	return max_price, median_price

def simulate_addgeneral(n_trials):
	max_diff, med_diff = [], []
	for dummy in range(n_trials):
		max_restricted, med_restricted = simulation(50, 30)
		max_unrestricted, med_unrestricted = simulation(40, 30)
		max_diff.append(max_restricted - max_unrestricted)
		med_diff.append(med_restricted - med_unrestricted)
	return sum(max_diff)/n_trials, sum(med_diff)/n_trials

def simulate_addcheaphousing(n_trials):
	max_diff, med_diff = [], []
	for dummy in range(n_trials):
		max_nolo, med_nolo = simulation(50, 30)
		max_lo, med_lo = simulation(50, 30, lower_quality_houses = 10) #more renters than houses; add low-end housing
		max_diff.append(max_nolo - max_lo)
		med_diff.append(med_nolo - med_lo)
	return sum(max_diff)/n_trials, sum(med_diff)/n_trials

def simulate_addexpensivehousing(n_trials):
	"""Return the mean change in maximum and median housing cost when
	high-end housing is added to a restricted market"""
	max_diff, med_diff = [], []
	for dummy in range(n_trials):
		max_nohi, med_nohi = simulation(50, 30)
		max_hi, med_hi = simulation(50, 30, higher_quality_houses = 10) #more renters than houses; add high-end housing
		max_diff.append(max_nohi - max_hi)
		med_diff.append(med_nohi - med_hi)
	return sum(max_diff)/n_trials, sum(med_diff)/n_trials

print simulate_addgeneral(100)
print simulate_addcheaphousing(100)
print simulate_addexpensivehousing(100)





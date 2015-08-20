import random

class Renter(object):

    def __init__(self, max_price, cbd_pref, new_pref, size_pref):
        """Constructor for Renter. 
        
        Args:
            max_price: maximum price they can pay in currency units.
            cbd_pref: degree to which they prefer a unit near the central business dist.
                real number between -1.0 and 1.0. 
            new_pref: degree to which they prefer a new unit. 
                real number between -1.0 and 1.0
            size_pref: degree to which they prefer a large unit. 
                real number between -1.0 and 1.0
        """
        self.max_price = max_price
        self.cbd_pref = cbd_pref
        self.new_pref = new_pref
        self.size_pref = size_pref
        
        self.renting = None  # house object
        
    def calc_match_score(self, housing_unit):
        """Calculates this Renter's score for a particular housing unit.
        
        Args:
            housing_unit: a HousingUnit object (defined below).
        
        Returns:
            A score in the range (-10, 10).
        """
        score = self.cbd_pref * housing_unit.cbd_prox
        score += self.new_pref * housing_unit.newness
        score += self.size_pref * housing_unit.size
        return score
        
    def set_matched(self, housing_unit):
        """Set my match to a particular housing unit.
        
        Args:
            h_unit: a HousingUnit object (defined below).
        """
        self.renting = housing_unit

    def clear_matched(self):
        """Clear my math to a the current housing unit.
        
        Clears my current rent price too.
        """
        self.renting = None
            

class RenterGenerator(object):
    
    def __init__(self, income_dist, cbd_dist, newness_dist, size_dist):
        """
        Distributions defined in distribution_objects.py
        
        Args:
            income_dist: distribution of incomes to sample from.
            cbd_dist: distribution of cdb proximity preferences to sample from. 
            newness_dist: distribution of newness preferences to sample from.
            size_dist: distribution of size preferences to sample from.
        """
        self.income_dist = income_dist
        self.cbd_dist = cbd_dist
        self.newness_dist = newness_dist
        self.size_dist = size_dist

    def generate_renters(self, n_renters):
        """Generates a list of N renters."""
        renters = []
        for _ in xrange(n_renters):
            income = self.income_dist.sample()
            max_price = income / 36.0
            cbd_pref = self.cbd_dist.sample()
            newness_pref = self.newness_dist.sample()
            size_pref = self.size_dist.sample()
        
            r = Renter(max_price, cbd_pref, newness_pref, size_pref)
            renters.append(r)
        return renters
        

class HousingUnit(object):
    def __init__(self, cbd_prox, newness, size):
        """Constructor for a HousingUnit.
        
        Args:
            cbd_prox: proximity to the central business district. 
                real number between 0.0 and 10.0. 
            newness: newness of construction.
                real number between 0.0 and 10.0.
            size: size of unit (arbitrary units).
                real number between 0.0 and 10.0.
        """
        self.current_price = 100
        self.cbd_prox = cbd_prox
        self.newness = newness
        self.size = size
        self.occupied = False
        self.rented_by = None

    def set_occupied(self, rented_by, auction_increment=1.05):
        self.current_price = int(self.current_price * auction_increment)
        self.rented_by = rented_by  # renter object
        self.occupied = True


class HousingUnitGenerator(object):
    
    def __init__(self, cbd_dist, newness_dist, size_dist):
        """
        Distributions defined in distribution_objects.py
        
        Args:
            cbd_dist: distribution of cdb proximity of units to sample from. 
            newness_dist: distribution of newness of units to sample from.
            size_dist: distribution of size of units to sample from.
        """
        self.cbd_dist = cbd_dist
        self.newness_dist = newness_dist
        self.size_dist = size_dist

    def generate_units(self, n_units):
        """Generates a list of N HousingUnits."""
        units = []
        for _ in xrange(n_units):
            cbd_prox = self.cbd_dist.sample()
            newness = self.newness_dist.sample()
            size = self.size_dist.sample()
        
            hu = HousingUnit(cbd_prox, newness, size)
            units.append(hu)
        return units

# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Created on: 6/6/15
# Created by: Jean-Ezra Yeung
# Matching by: Phil Nova

# Outline
# 1. Objects - Generate 2 lists: renters, houses
# 2. Emergence - Match renters and houses based on price and niceness (quality for acceptance)
# 3. Complexity

import random

# 1. Objects - Generate 2 lists: renters, houses
def rent_list():
    renters = list(range(1,10))
    return renters

def house_list():
    houses = list(range(1,10))
    return houses

# 2. Emergence - Match renters and houses based on price and niceness (quality for acceptance)

def score(renter, list_of_houses):
    """Return ordered list of indices for the renter's preferences on houses.
    E.g. return [0,3,2,1] if renter prefers list_of_houses[0] most, etc."""
    pass

class Renter(object):
    def __init__(self, willingness_to_pay, niceness_threshold, min_rooms, ID):
        self.ID = ID #integer representing order in an array
        self.willingness_to_pay = willingness_to_pay
        self.niceness_threshold = niceness_threshold
        self.min_rooms = min_rooms
        self.housing_preference_list = []
        self.__matched = False

    def get_matched(self):
        return self.__matched

    def set_matched(self, matched = True):
        self.__matched = matched

    def order_houses_test(self, house_list):
        self.housing_preference_list = range(len(house_list))

class House(object):
    def __init__(self, rent, niceness, num_rooms):
        self.rent = rent
        self.niceness = niceness
        self.num_rooms = num_rooms
        self.rented_for = float("inf")
        self.__occupied = False
        self.rented_by = None

    def get_occupied(self):
        return self.__occupied

    def set_occupied(self, rented_for, rented_by, occupied = True):
        self.rented_for = rented_for #current rent price
        self.rented_by = rented_by #integer ID of renter
        self.__occupied = True

def stable_match(renters, houses):
    """Gale-Shapley stable matching algorithm.
    In each round, renters (in random order) bid their maximum WTP for their most preferred house. All bids exceeding the
    asking price are accepted. If a higher bid is offered, the current renter is evicted.
    In subsequent rounds, all unmatched renters proceed as before. This continues until all renters are matched."""
    
    while True:
        flag = False #keep track of whether any houses changed hands

        #randomize order of renters
        random.shuffle(renters)
        for r in renters:
            if not r.get_matched():
                for house_index in r.housing_preference_list:
                    house = houses[house_index]
                    if not house.get_occupied() or r.willingness_to_pay > house.rented_for:
                        #either house is unoccupied or renter outbids current occupant

                        if house.rented_by != None: #someone was already in apartment
                            renters[house.rented_by].set_matched(False) #old renter is evicted

                        house.rented_by = r.ID
                        r.set_matched() #renter moves in
                        house.set_occupied(r.willingness_to_pay, r.ID)
                        flag = True

        if not flag: #no houses changed hands; we are done
            return 



###TEST FUNCTIONS
def create_test(n_renters):
    #create lots of houses with same price: $100
    house_list = [House(100,1,1) for dummy in range(n_renters)]
    renter_list = [Renter(100+dummy,1,1,dummy) for dummy in range(n_renters)]
    for r in renter_list:
        r.order_houses_test(house_list)
        #print r.ID
    stable_match(renter_list, house_list)
    for house in house_list:
        print house.rented_by

if __name__ == "__main__":
    create_test(10)    

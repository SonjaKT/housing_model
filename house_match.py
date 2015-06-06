# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Created by: Phil Nova

import random

class Renter(object):
    def __init__(self, willingness_to_pay, ID):
        self.ID = ID #integer representing order in an array
        self.willingness_to_pay = willingness_to_pay
        self.paying = 0
        self.housing_preference_list = []
        self.__matched = False

    def get_matched(self):
        return self.__matched

    def set_matched(self, matched = True):
        self.__matched = matched

    def order_houses_test(self, house_list):
        self.housing_preference_list = range(len(house_list))

class House(object):
    def __init__(self, niceness):
        self.current_price = 100
        self.niceness = niceness
        self.__occupied = False
        self.rented_by = None

    def get_occupied(self):
        return self.__occupied

    def set_occupied(self, rented_by, occupied = True, auction_increment = 1.05):
        self.current_price = self.current_price * auction_increment
        self.rented_by = rented_by #integer ID of renter
        self.__occupied = True

def stable_match(renters, houses, increment = 1.05):
    """Gale-Shapley stable matching algorithm.
    In each round, renters (in random order) bid their maximum WTP for their most preferred house. All bids exceeding the
    asking price are accepted. If a higher bid is offered, the current renter is evicted.
    In subsequent rounds, all unmatched renters proceed as before. This continues until all renters are matched.
    Houses should be ordered from highest to lowest scores."""

    while True:

        flag = False #keep track of whether any houses changed hands

        for r in renters:
            if not r.get_matched():
                for house in houses: #must be ordered by quality!
                    if r.willingness_to_pay > house.current_price * increment:
                        #either house is unoccupied or renter outbids current occupant

                        if house.rented_by != None: #someone was already in apartment
                            renters[house.rented_by].set_matched(False) #old renter is evicted

                        house.rented_by = r.ID
                        r.set_matched() #renter moves in
                        house.set_occupied(r.ID, auction_increment = increment)
                        r.paying = house.current_price
                        flag = True
                        break

        if not flag: #no houses changed hands; we are done
            return 


###TEST FUNCTIONS
def create_test(n_renters):
    #create lots of houses with same price: $100
    house_list = [House(1) for dummy in range(n_renters)]
    renter_list = [Renter(150-dummy,dummy) for dummy in range(n_renters)]
    for r in renter_list:
        r.order_houses_test(house_list)
        #print r.ID
    stable_match(renter_list, house_list)
    for renter in renter_list:
        print renter.willingness_to_pay, renter.paying

if __name__ == "__main__":
    create_test(10)    

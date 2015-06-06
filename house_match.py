# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Created by: Phil Nova

import random
from classes import *

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

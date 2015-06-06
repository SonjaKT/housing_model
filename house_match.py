# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Created by: Phil Nova

import random
from classes import *
import sorting

def sort_houses_by_niceness(house_list):
    bl = sorting.BasicList(house_list)
    return bl.merge_sort()[::-1] #from most to least nice


def stable_match(renters, houses, increment = 1.05):
    """Gale-Shapley stable matching algorithm.
    In each round, renters (in random order) bid their maximum WTP for their most preferred house. All bids exceeding the
    asking price are accepted. If a higher bid is offered, the current renter is evicted.
    In subsequent rounds, all unmatched renters proceed as before. This continues until all renters are matched.
    Houses should be ordered from highest to lowest scores."""

    houses = sort_houses_by_niceness(houses)

    while True:

        flag = False #keep track of whether any houses changed hands

        for r in renters:
            if not r.get_matched():
                for house in houses: #must be ordered by quality!
                    if r.willingness_to_pay > house.current_price * increment:
                        #either house is unoccupied or renter outbids current occupant

                        if house.rented_by != None: #someone was already in apartment
                            renters[house.rented_by].set_matched(False) #old renter is evicted
                            renters[house.rented_by].paying = 0 

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
    house_list = [House(dummy) for dummy in range(n_renters)]
    renter_list = [Renter(1000-dummy*10,dummy) for dummy in range(n_renters)]
    for r in renter_list:
        r.order_houses_test(house_list)
        #print r.ID
    stable_match(renter_list, house_list)
    for house in house_list:
        print house.niceness, renter_list[house.rented_by].willingness_to_pay, renter_list[house.rented_by].paying

if __name__ == "__main__":
    create_test(10)    

# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Created by: Phil Nova

import random
from classes import *
import sorting
import random

def sort_houses_by_niceness(house_list):
    bl = sorting.BasicList(house_list)
    return bl.merge_sort()[::-1] #from most to least nice

def stable_match(renters, houses, increment = 1.05, k = 10):
    """
    Gale-Shapley stable matching algorithm:
    In each round, renters bid for their most preferred house. All bids exceeding the
    asking price are accepted. If a higher bid is offered, previous renter is kicked out.
    In subsequent rounds, all unmatched renters proceed as before. This continues until all renters are matched.

    We make the simplifying assumption that all renters share the same preferences for houses.
    We also assume that renters want the highest-quality house with price below their maximum
    willingness to pay.

    increment is how much a potential renter must outbid the previous highest
    k is the number of randomly selected apartments each renter considers
    """

    houses = sort_houses_by_niceness(houses)

    while True:

        flag = False #keep track of whether any houses changed hands

        for r in renters:
            if not r.matched:
                for house in sorted(random.sample(houses, k), reverse=True):
                    if r.willingness_to_pay > house.current_price * increment:
                        #either house is unoccupied or renter outbids current occupant

                        if house.rented_by != None: #someone was already in apartment
                            house.rented_by.set_matched(None, False) #old renter is evicted
                            house.rented_by.paying = 0 

                        house.rented_by = r
                        r.set_matched(house) #renter moves in
                        house.set_occupied(r, auction_increment = increment)
                        r.paying = house.current_price
                        flag = True
                        break

        if not flag: #no houses changed hands; we are done
            return 

if __name__ == "__main__":
    create_test(10)    

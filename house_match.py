# Project: SF BARF
# Goal: Create a matching function for renters and houses
# Created by: Phil Nova
# Modified by Matt Lichti

import random
from classes import *
import random


def stable_match(renters, houses, increment=1.05, k=20):
    """
    Matching based on Gale-Shapley stable matching algorithm:
    In each round, renters bid for their most preferred house out of k
    randomly selected houses. If the bid exceeds the previous highest offer,
    it becomes the new highest offer. In subsequent rounds, all unmatched
    renters proceed as before. This continues until all renters are matched.

    We make the simplifying assumption that all renters share the same
    preferences for houses. We also assume that renters want the
    highest-quality house with price below their maximum willingness to pay.

    increment is how much a potential renter must outbid the previous highest
    k is the number of randomly selected apartments each renter considers.
    """
    k = min(k, len(houses))
    while True:
        flag = False  # keep track of whether any houses changed hands
        for r in renters:
            if not r.matched:
                for house in sorted(random.sample(houses, k), reverse=True):
                    if house.score >= r.min_score and (r.willingness_to_pay >
                                                       house.current_price *
                                                       increment):
                        # either house is unoccupied or
                        # renter outbids current occupant
                        if house.rented_by is not None:  # already an offer
                            house.rented_by.set_matched(None, False)
                            house.rented_by.paying = 0
                        house.rented_by = r
                        r.set_matched(house)  # renter moves in
                        house.set_occupied(r, auction_increment=increment)
                        r.paying = house.current_price
                        flag = True
                        break

        if not flag:  # no houses changed hands; we are done
            return

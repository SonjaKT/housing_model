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
            if r.renting:
                # They currently have a bid in on a unit.
                continue 
            
            random_unit_sample = random.sample(houses, k)
            scores_and_units = [(r.calc_match_score(hu), hu) for hu in random_unit_sample]
            sorted_unit_sample = sorted(scores_and_units, reverse=True)
            
            for personal_score, h_unit in sorted_unit_sample:
                if r.max_price > h_unit.current_price * increment:
                    if h_unit.rented_by: 
                        # house currently has a bid.
                        h_unit.rented_by.clear_matched()
                    
                    h_unit.set_occupied(r, auction_increment=increment)
                    r.set_matched(h_unit)
                    
                    flag = True
                    break

        if not flag:  # no houses changed hands; we are done
            return

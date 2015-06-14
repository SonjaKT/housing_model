class Renter(object):

    def __init__(self, willingness_to_pay, min_score):
        self.willingness_to_pay = willingness_to_pay
        self.paying = 0
        self.housing_preference_list = []
        self.matched = False
        self.renting = None  # house object
        self.min_score = min_score

    def set_matched(self, house=None, matched=True):
        self.matched = matched
        self.renting = house  # house object


class House(object):
    def __init__(self, score):
        self.current_price = 100
        self.score = score
        self.occupied = False
        self.rented_by = None

    # override comparison operators so we can do sorting
    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score

    def set_occupied(self, rented_by, occupied=True, auction_increment=1.05):
        self.current_price = int(self.current_price * auction_increment)
        self.rented_by = rented_by  # renter object
        self.occupied = True

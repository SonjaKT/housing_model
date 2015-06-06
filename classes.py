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

    def __lt__(self, other):
        return self.niceness < other.niceness

    def __gt__(self, other):
        return self.niceness > other.niceness

    def __le__(self, other):
        return self.niceness <= other.niceness

    def __ge__(self, other):
        return self.niceness >= other.niceness

    def __eq__(self, other):
        return self.niceness == other.niceness

    def get_occupied(self):
        return self.__occupied

    def set_occupied(self, rented_by, occupied = True, auction_increment = 1.05):
        self.current_price = self.current_price * auction_increment
        self.rented_by = rented_by #integer ID of renter
        self.__occupied = True


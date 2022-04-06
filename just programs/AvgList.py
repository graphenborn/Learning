from statistics import (median, median_high, median_low)

class AvgList(list):

    def __init__(self, list):
        self.list = list

    def mean(self):
        return sum(self.list) / len(self.list)

    def median(self):
        return median(self.list)

    def median_low(self):
        return median_low(self.list)

    def median_high(self):
        return median_high(self.list)
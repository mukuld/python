# Python Programme Number 86
# Magic Methods: Subclassing List function to create a counter
# Programmer: Mukul Dharwadkar
# Date: 11 June 2009

class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

# Python Programme Number 79
# Story to demonstrate parameter collector
# Programmer: Mukul Dharwadkar
# Date: 20 August 2008

def interval(start, stop=None, step=1):
    "Imitates range() for step > 0"
    if stop is None:            # If the stop is not supplied
        start, stop = 0, start  # shuffle the parameters
    result = []
    i = start                   # We start counting at the index
    while i < stop:             # until the index reaches the stop index...
        result.append(i)        # ...append the index to the result...
        i += step               # ...increment the index with the step (>0)
    return result


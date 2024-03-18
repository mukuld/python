# Python Programme Number 82
# Another implementation of recursive functions to carry out a binary search
# Programmer: Mukul Dharwadkar
# Date: 08 June 2009

def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

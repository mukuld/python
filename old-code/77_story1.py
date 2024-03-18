# Python Programme Number 77
# Story to demonstrate parameter collector
# Programmer: Mukul Dharwadkar
# Date: 19 August 2008

def story(**kwds):
    return "Once upon a time, there was a "\
           "%(job)s called %(name)s." % kwds

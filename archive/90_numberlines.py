# Python Programme Number 90
# File handling
# Programmer: Mukul Dharwadkar
# Date: 17 June 2009

import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print "%-40s # %2i" % (line, num)

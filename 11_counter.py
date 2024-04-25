# Python Programme Number 11
# Counter - Demonstration of break and continue statements
# Programmer: Mukul Dharwadkar
# Date: 24 February 2006

count = 0
while True:
    count += 1
    # Loop should end if count is greater than 10
    if count > 10:
        break
    # We want to skip the number 5
    if count == 9:
        continue
    print count


#raw_input("\n\nPress enter to exit.")

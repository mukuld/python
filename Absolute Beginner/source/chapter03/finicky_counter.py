# Finicky Counter
# Demonstrates the break and continue statements
# Michael Dawson - 1/3/03

count = 0
while True:
    count += 1
    # end loop if count greater than 10
    if count > 10:
       break
    # skip 5
    if count == 5:
        continue
    print count
    
raw_input("\n\nPress the enter key to exit.")

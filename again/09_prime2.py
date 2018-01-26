'''
Created on Apr 24, 2013

@author: mdharwadkar
'''
num = int(raw_input("Enter the number till which you want to find prime numbers > "))
orig_num = num
count = 0

for n in range(2, num):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print n, "is a prime number"
        count += 1
print "There are", count, "prime numbers in the first", num, "numbers\n"

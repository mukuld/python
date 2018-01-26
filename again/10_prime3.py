'''
Created on Apr 24, 2013

@author: mdharwadkar
'''
from sys import exit
num = raw_input("Enter the number till which you want to find prime numbers > ")
#num = int(num)
if isinstance(int(num), int):
    num = int(num)
    orig_num = num
    count = 0
    for n in range(2, num):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print n, "is a prime number"
            count += 1
else:
    print "Please enter a number next time."
    exit(0)
print "There are", count, "prime numbers in the first", num, "numbers\n"

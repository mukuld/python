'''
Created on Apr 24, 2013

@author: mdharwadkar
'''

num = 200;
num_orig = num
count = 0;

while num > 0:
    if num % 2 == 0:
        div = int(num / 2)
    else:
        div = (int(num / 2) + 1)
    while div > 0:
        if div == 1: 
            print "Number", num, "is prime\n"
            count += 1
            break
        else:
            result = num % div
            if result == 0:
                break
                div -= 1
            else:
                div -= 1
    num -= 1
    if num == 1:
        break
print "In all there are", count, "prime numbers in the first", num_orig, "numbers\n"

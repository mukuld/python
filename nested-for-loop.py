#########################################
# Implement nested for loops in Python  #
# Programmer: Mukul Dharwadkar          #
# Date: 24 September 2021               #
#########################################

a = 0
#c=1
for i in range(10):
    for j in range(6):
        c=1
        for k in range(1, 17, c):
            while c < 17:
               # print(f'Index c is {c}')
                c = c * 2
                #print(f"Index i is {i}")
                #print(f"Index j is {j}")
                a += 1
            #print(f"The value of a when is i, j, k and c is {i}, {j}, {k}, {c} is {a}")
print(f'The value of a is {a}')
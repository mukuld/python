num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

#Find multiples of the number
factors1 = []
factors2 = []
for i in range(5):
    f1 = num1 * (i + 1)
    f2 = num2 * (i + 1)
    factors1.append(f1)
    factors2.append(f2)
    fc1 = set(factors1)
    fc2 = set(factors2)
    LCM = (fc1 & fc2)
    if (LCM):
        print("The LCM of ", num1, "and ", num2, "is ", LCM)
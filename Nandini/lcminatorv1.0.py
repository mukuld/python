def set_number_quantity():
    quantity = int(input("How many numbers do you want to find LCM for: "))
    return quantity

def ask_numbers():
    quantity = set_number_quantity()
    for i in range(quantity):
        num[i + 1] = int(input("Please enter a number: "))
        return num[i + 1]

#Find multiples of the number
def find_lcm(n1, n2):
        factors1 = []
        factors2 = []
        for i in range(5):
                f1 = n1 * (i + 1)
                f2 = n2 * (i + 1)
                factors1.append(f1)
                factors2.append(f2)
                fc1 = set(factors1)
                fc2 = set(factors2)
                LCM = (fc1 & fc2)
                if (LCM):
                        print("The LCM of ", n1, "and ", n2, "is ", LCM)
def main():
        num1, num2 = ask_numbers()
        find_lcm(num1, num2)
    
main()
def ask_numbers():
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        return num1, num2

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
                        print("The LCM of ", n1, "and ", n
                        2, "is ", LCM)
def main():
        num1, num2 = ask_numbers()
        find_lcm(num1, num2)
    
main()
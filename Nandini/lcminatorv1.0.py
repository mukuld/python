def set_number_quantity():
        """
        The set_number_quantity function allows the user to set the quantity of numbers for
        which LCM needs to be determined.
        """
    quantity = int(input("How many numbers do you want to find LCM for: "))
    return quantity

def ask_numbers():
        """The ask_numbers function is an input function for the program where it asks
        the user to enter the numbers of which the LCM needs to be determined."""
    quantity = set_number_quantity()
    #print (quantity)
    #Quantity is already in the function set_number_quantity, so why is it in the function ask_numbers?
    var_dict = {}
    #What is var?
    for i in range(quantity):
        #print (i)
        var_dict["num" + str(i+1)] = int(input("Please enter a number: "))
        #nums.append(num[i+1])
        #Won't num appear as a string in the output? Like, numPlease enter a number:
    return list(var_dict.values())

#Find multiples of the number
def find_lcm(num_list):
        list_len = len(num_list)
        print ("The length of the list is: ", list_len)
        print ("The list of numbers is: ", num_list)
        for x in range(list_len):
                print ("The ", (x+1), "th number is: ", num_list[x])
        var_dict1 = {}
        var_dict2 = {}
        for j in range(list_len):
            var_dict1["factors" +str(j+1)] = []
        print (list(var_dict1.keys()))
        print (list(var_dict1.values()))
        #factors1 = []
        #factors2 = []
        for i in range(list_len):
            print (i)
            for k in range(5):
                print ("Outer counter is: ", i)
                #What is outer counter?
                print ("Counter is:", k)
                print ("Multipying", num_list[i], "with ", (k + 1), " = ", (num_list[i] * (k + 1)))
                var_dict2["f" + str(k+1)] = num_list[i] * (k + 1)
                #list(var_dict1.keys()[i])) = []
                #print (factors[i])
        print (list(var_dict2.values()))
        print (list(var_dict2.keys()))
        #        f2 = n2 * (i + 1)
        #        factors1.append(f1)
        #        factors2.append(f2)
        #        fc1 = set(factors1)
        #        fc2 = set(factors2)
        #        LCM = (fc1 & fc2)
        #        if (LCM):
        #                print("The LCM of ", n1, "and ", n2, "is ", LCM) 
def main():
        numbers = ask_numbers()
        print ("Numbers are:", numbers)
        find_lcm(numbers)
        #print(numbers)
    
main()
#Program to find LCM of given two numbers
#Date: 30 Oct 2018
#Programmer: Mukul Dharwadkar

def check_multiples_equality(n1, n2):
	num1 = n1
	num2 = n2
	
	if num1 == num2:
		return num1

def find_muliples(number):
	n = 1
	while true:
		number = number * n
		n++
		return number

def main():
	int number1 = raw_input("Please enter the first number: ")
	int number2 = raw_input("Please enter the second number: ")
	
	while number1 != number2:
		find_multiples(number1)
		find_multiples(number2)
		check_multiples_equality(number1, number 2)
	print "The LCM of ", number1, " and ", number2, "is ", number1 "."
	
main()
	
		
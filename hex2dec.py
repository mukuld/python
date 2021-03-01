# Program to convert a hexadecimal number to decimal

MULTIPLIER = 16
hex_letters = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}

def get_keys(dict):
    return list(dict.keys())

def get_number():
    number = input("Please enter a hexadecimal number: ")
    return number

#def get_length(n):
#    length = len(str(n))
#    return length

def convert(num):
    letters = get_keys(hex_letters)
    hex_num = 0
    count = 0
    for n in num:
        rev_num = num[::-1]
        if n in letters:
            digit = hex_letters.get(n)
            i = rev_num.index(n)
            hex_num = hex_num + (int(digit) * pow(16, i))
#    while num:
#        digit = num % 10
#        hex_num = hex_num + (digit * pow(16, count))
#        num = int(num / 10)
#        count += 1
    print(hex_num)

def main():
    convert(get_number())
main()
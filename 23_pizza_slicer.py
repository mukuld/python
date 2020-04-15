# Python Programme Number 23
# Pizza Slicer: Demonstrates slicing technique for strings
# Programmer: Mukul Dharwadkar
# Date: 6 March 2006

word = "pizza"

print \
      """
      Slicing 'Cheat Sheet'

      0   1   2   3   4   5
      +---+---+---+---+---+
      | p | i | z | z | a |
      +---+---+---+---+---+
       -5  -4  -3  -2  -1

       """
print "Enter the beginning and ending index for your slice of 'pizza'."
print "Press the enter key at 'Begin' to exit."

begin = None
while begin != "":
    begin = raw_input("\nBegin: ")

    if begin:
        begin = int(begin)

        end = input("End: ")

        print "word[", begin, ":", end, "]\t\t",
        print word[begin:end]

raw_input("Press enter to exit.")

# Python Programme Number 50
# Write It: Demostrates writing to a text file
# Programmer: Mukul Dharwadkar
# Date: 14 April 2006

# Demonstrating the write() method.
print "Creating a text file with the write() method."
text_file = open("/home/mukul/src/python/write_it.txt", "w")

text_file.write("Line 1\n")
text_file.write("This is Line 2\n")
text_file.write("That makes this line 3\n")

text_file.close()

# Testing the success of the method
print "\nReading from the file just created.\n"
text_file = open("/home/mukul/src/python/write_it.txt", "r")
print text_file.read()
text_file.close()

# Demonstrating the writelines() method.
print "\nCreating a text file with the writelines() method."
text_file = open("/home/mukul/src/python/write_it_lines.txt", "w")

lines = ["Line 1\n",
         "This is line 2\n",
         "This makes this line 3\n"]

text_file.writelines(lines)
text_file.close()

# Testing the success of the method
print "\nReading from the newly created file."
text_file = open("/home/mukul/src/python/write_it_lines.txt", "r")
for line in text_file:
    print line

text_file.close()

raw_input("\n\nPress enter to exit.")

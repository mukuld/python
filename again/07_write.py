# Program to write to a file
# Programmer: Mukul Dharwadkar
# Date: Nov 5 2012

file_name = raw_input("What is the name of the file you want to write to: ")
text_file = open(file_name, "a+")

thoughts="temp"

while thoughts:
    thoughts = raw_input("What are your thoughts? (Enter to exit): ")
    text_file.write(thoughts)
    text_file.write("\n")
    
print "Thank you for your thoughts!!"
    
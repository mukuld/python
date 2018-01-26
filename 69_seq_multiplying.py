# Python Programme Number 69
# Sequence Multiplication demonstration programme
# Programmer: Mukul Dharwadkar
# Date: 6th December 2006

# Prints a sentence in a centered box of correct width

sentence = raw_input("Write your thoughts in one line: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) / 2

print
print " " * left_margin + "+"     + "-" * (box_width + 2)+    "+"
print " " * left_margin + "|    " + " " * text_width     +"    |"
print " " * left_margin + "|    " +       sentence       +"    |"
print " " * left_margin + "|    " + " " * text_width     +"    |"
print " " * left_margin + "+"     + "-" * (box_width + 2)+    "+"
print

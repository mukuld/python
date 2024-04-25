# Python Program Number 28
# Backward printing: Implementing strings
# Programmer: Mukul Dharwadkar
# Date: 8 March 2006

message = raw_input("Send your message to the world: ")

position = len(message)
new_message = ""

while position:
    new_message += message[position-1]
    position -= 1

print new_message

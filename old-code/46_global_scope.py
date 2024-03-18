# Python Programme Number 46
# Global reach: Demonstrates the concept of Global variable
# Programmer: Mukul Dharwadkar
# Date: 31 March 2006

def read_global():
    print "From inside the local scope of read_global(), value is: ", value

def shadow_global():
    value = -10
    print "From inside the local scope of shadow_global(), value is: ", value

def change_global():
    global value
    value = -10
    print "From inside the local scope of change_global(), value is: ", value

# main
# The variable value is a global variable because we are defining it in the
# global scope here

value = 10
print "In the global scope, value has been set to: ", value

read_global()
print "Back in the global scope, value is still: ", value

shadow_global()
print "Back in the global scope, value is still:", value

change_global()
print "Back in the global scope, value has now changed to:", value

raw_input("\nPress enter to exit.")

# Global Reach
# Demonstrates global variables
# Michael Dawson - 2/21/03

def read_global():
    print "From inside the local namespace of read_global(), value is:", value

def shadow_global():
    value = -10
    print "From inside the local namespace of shadow_global(), value is:", value
  
def change_global():
    global value
    value = -10
    print "From inside the local namespace of change_global(), value is:", value

# main
# value is a global variable because we're in the global namespace here
value = 10
print "In the global namespace, value has been set to:", value, "\n"

read_global()
print "Back in the global namespace, value is still:", value, "\n"

shadow_global()
print "Back in the global namespace, value is still:", value, "\n"

change_global()
print "Back in the global namespace, value has now changed to:", value

raw_input("\n\nPress the enter key to exit.")











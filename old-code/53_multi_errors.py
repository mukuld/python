# Python Programme Number 53
# Handling mutliple errors
# Programmer: Mukul Dharwadkar
# Date: 23 June 2006

print
for value in (None, "Hi", 65):
    try:
        print "Attempting to convert", value, "->",
        print float(value)
    except(TypeError):
        print "I can handle only a string or a number, not a null."
    except(ValueError):
        print "I can handle only numbers and characters..."

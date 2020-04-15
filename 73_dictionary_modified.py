# Python Programme Number 73
# Dictionary demonstration programme
# Programmer: Mukul Dharwadkar
# Date: 7th December 2006

# Create a sample database of name and numbers with addresses using get()

# A dictionary with person names as keys. Each person is represented as another
# dictionary with the keys "phone" and "addr" referring to their phone number
# and address respectively

people = {
    "Mukul":{
        "phone": "7569",
        "addr": "450 Holger way"
        },
    "Shital":{
        "phone": "1876",
        "addr": "3707 Poinciana Drive"
        },
    "Barnali":{
        "phone": "9212",
        "addr": "Bangalore, India"
        }
    }

# Descriptive labels for the phone number and address. These will be used
# when printing the output.

labels = {
    "phone": "Phone Number",
    "addr": "Address"
    }

name = raw_input("Name: ")
if name in people:
    # Are we looking for name or address
    request = raw_input("Phone Number (p) or Address (a)?")

    # Use the correct key
    key = request       # In case the request is neither "p" nor "a"
    if request.lower() == "p":
        key = "phone"
    if request.lower() == "a":
        key = "addr"

    # Use get to provide default values:
    person = people.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, "not available")

    # Only try to print the information if the name is valid key in our dictionary

    print "%s's %s is %s." % (name, label, result)
else:
    print "Name not found in database"

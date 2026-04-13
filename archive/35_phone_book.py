# Python Programme Number 35
# The Phone Book
# Programmer: Mukul Dharwadkar
# Date: 19 March 2006

# Create an empty dictionary
phonebook = {}

choice = None
while choice != "0":

    print \
          """
          Geek Translator

          0 - Quit
          1 - Look Up a Phone number
          2 - Add a phone number
          3 - Modify a phone number
          4 - Delete a phone number
          """
    choice = raw_input("Make a choice: ")
    print

    # Exit clause
    if choice == "0":
        print "Goodbye!"

    # Get a definition
    elif choice == "1":
        term = raw_input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print "\n", term, "means", definition
        else:
            print "\nSorry, I don't know", term

    # Add a term-definition pair
    elif choice == "2":
        term = raw_input("What term do you want me to add?: ")
        if term not in geek:
            definition = raw_input("What's the definition?: ")
            geek[term] = definition
            print "\n", term, "has been added."
        else:
            print "\nThat term already exists! Try redefining it."

    # Redefine an existing term
    elif choice == "3":
        term = raw_input("What term do you want me to redefine?: ")
        if term in geek:
            definition = raw_input("What's the new definition?: ")
            geek[term] = definition
            print "\n", term, "has been redefined."
        else:
            print "\nThat term doesn't exist! Try adding it."

    # Delete a term-definition pair
    elif choice == "4":
        term = raw_input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print "\nOkay. I have deleted", term
        else:
            print "I can't do that", term, "doesn't exist in the dictionary."

    # Handle invalid choice
    else:
        print "\nSorry, but", choice, "isn't a valid choice."

raw_input("\n\nPress enter to exit.")

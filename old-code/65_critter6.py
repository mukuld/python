# Python Programme Number 65
# Critter Caretaker: A virtual pet to care for
# Programmer: Mukul Dharwadkar
# Date: 4 July 2006
# This programme allows the user to decide the amount of food or time spent
# playing with the critter. This will directly affect the hunger and
# boredom levels of the critter.

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "happy"
        elif 5 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "mad"
        return mood
    
    def __str__(self):
        print "I am ", self.boredom, "bored"
        print "I am ", self.hunger, "hungry and I am", self.mood

    mood = property(__get_mood)

    def talk(self):
        print "I'm", self.name, "and I feel", self.mood, "now\n"
        self.__pass_time()

    def eat(self, food = 4):
        food = input("How much food would like to feed the critter?: ")
        print "Buurrp, Thank you"
        self.hunger -= int(food)
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        fun = input("How much time would you want to spend playing with the critter?: ")
        print "Wheee!!!"
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = raw_input("What do you want to name your critter?: ")
    pet = Critter(crit_name)

    # Create the menu which allows the user to interact with his / her virtual pet

    choice = None
    while choice != "0":
        print \
              """
              Critter Caretake

              0 - Quit
              1 - Listen to your critter
              2 - Feed your critter
              3 - Play with your critter
              """

        choice = raw_input("Choice: ")
        print

        # exit
        if choice == "0":
            print "Good-bye"

        # Listen to your critter
        elif choice == "1":
            pet.talk()

        # Feed your critter
        elif choice =="2":
            pet.eat()

        # Play with your critter
        elif choice == "3":
            pet.play()

        # Hidden choice
        elif choice == "99":
            pet.__str__()
        # Invalid choice
        else:
            print "\nSorry, but", choice, "isn't a valid choice."

main()
raw_input("\n\nPress enter to exit")

# Python Programme Number 66
# Simulate a Television set
# Programmer: Mukul Dharwadkar
# Date: 8 September 2006
# Final Date: 9 June 2009

class Television(object):
    """A virtual Telly"""
    def __init__(self, channel=1, volume=10):
        self.channel = channel
        self.volume = volume
        """ Empty module"""
    
    def chg_chn(self):
        self.channel = input("Please select the channel you want to watch: ")
        while self.channel > 100 or self.channel < 0:
            print "Please enter a valid number."
            self.channel = input("Please select the channel you want to watch: ")
        return self.channel

    def chg_vol(self):
        self.volume = input("Please select the volume level: ")
        while self.volume > 60 or self.volume < 0:
            print "Please enter a valid number."
            self.volume = input("Please select the volume level: ")
        return self.volume

    #volume = property(chg_vol)

    def chn(self, channel=1):
        print "Currently you are watching channel no: ", self.channel
        #self.channel()
    def vol(self):
        volume = self.volume
        print "The volume level is: ", self.volume

def main():
    """This is the main module and will call the other modules"""
    tv = Television()

    choice = None
    while choice != "0":
        print \
              """
                Television Menu

                0 - Switch Off
                1 - Select Channel to watch
                2 - Select volume level
                3 - Display channel
                4 - Display volume level
                """

        choice = raw_input("Make your selection: ")
        print

        #Switch Off
        if choice == "0":
            print "Good Bye"

        # Change the channel
        elif choice == "1":
            tv.chg_chn()

        elif choice == "2":
            tv.chg_vol()

        elif choice == "3":
            tv.chn()

        elif choice == "4":
            tv.vol()

        else:
            print "\nSorry, but", choice, "isn't a valid selection."

main()
#raw_input("\n\nPress enter to exit") 
    

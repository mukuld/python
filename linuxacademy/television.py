class Television:
    """
    A class to create a simulation of a Television
    """
    
    def __init__(self, volume = 10, channel = 1):
        self.volume = volume
        self.channel = channel

    def description(self):
        print(f"This is a television showing channel number {self.channel} at {self.volume} volume level")

    def change_channel(self):
        self.channel = int(input("Please select a channel: "))
        while self.channel not in range(100):
            print(f"Sorry, that channel is not available, try again.")
            self.channel = int(input("Please select a channel: "))
        return self.channel

    def change_volume(self):
        self.volume = int(input("Please select volume level: "))
        while self.volume not in range(50):
            print(f"Sorry, invalid volume selection. Try again")
            self.volume = int(input("Please select volume level: "))
        return self.volume

    def show_channel(self, channel = 1):
        channel = self.channel
        print(f"You are currently watching channel number {self.channel}")

    def show_volume(self, volume = 1):
        volume = self.volume
        print(f"The volume level is at {self.volume}")

def main():
    """
    This is the main module of the program that instantiates the class Television
    """

    tv = Television()

    choice = None
    while choice is not "0":
        print(\
            """
            Television Menu
            
            0 = Switch Off
            1 = Change channel
            2 = Change Volume
            3 = Show current channel
            4 = Show current volume
            """)
        
        choice = input("Make your selection: ")
        print()

        if choice == "0":
            print("Good bye")
        elif choice == "1":
            tv.change_channel()
        elif choice == "2":
            tv.change_volume()
        elif choice == "3":
            tv.show_channel()
        elif choice == "4":
            tv.show_volume()
        else:
            print("\nInvalid choice. Try again")

main()

# Sound and Music
# Demonstrates playing sound and music files
# Michael Dawson 5/18/03

from livewires import games

# load a sound file
missile = games.load_sound("missile.wav")

#load the music file
games.load_music("theme.mid")

choice = None
while choice != "0":

    print \
    """
    Sound and Music
    
    0 - Quit
    1 - Play missile sound
    2 - Loop missile sound
    3 - Stop missile sound
    4 - Play theme music
    5 - Loop theme music
    6 - Stop theme music
    """
    
    choice = raw_input("Choice: ")
    print

    # exit
    if choice == "0":
        print "Good-bye."

    # play missile sound
    elif choice == "1":
        missile.play()
        print "Playing missile sound."

    # loop missile sound
    elif choice == "2":
        loop = int(raw_input("Loop how many extra times? (-1 = forever): "))
        missile.play(loop)
        print "Looping missile sound."

    # stop missile sound
    elif choice == "3":
        missile.stop()
        print "Stopping missile sound."

    # play theme music
    elif choice == "4":
        games.play_music()
        print "Playing theme music."

    # loop theme music
    elif choice == "5":
        loop = int(raw_input("Loop how many extra times? (-1 = forever): "))
        games.play_music(loop)
        print "Looping theme music."

    # stop theme music
    elif choice == "6":
        games.stop_music()
        print "Stopping theme music."
                 
    # some unknown choice
    else:
        print "\nSorry, but", choice, "isn't a valid choice."
  
raw_input("\n\nPress the enter key to exit.")

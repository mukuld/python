# New Graphics Window
# Demonstrates creating a graphics window
# Michael Dawson 5/9/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
my_screen.mainloop()

# Pretty Graphics Window
# Demonstrates setting the background image of a graphics screen
# Michael Dawson 5/9/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

my_screen.mainloop()

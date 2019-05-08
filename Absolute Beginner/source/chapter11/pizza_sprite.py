# Pizza Sprite
# Demonstrates creating a sprite 
# Michael Dawson 5/9/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Pizza(games.Sprite):
    """ A pizza sprite. """
    def __init__(self, screen, x, y, image):
        """ Initialize pizza object. """
        self.init_sprite(screen = screen, x = x, y = y, image = image)

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

pizza_image = games.load_image("pizza.bmp")
Pizza(screen = my_screen,
      x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
      image = pizza_image)

my_screen.mainloop()

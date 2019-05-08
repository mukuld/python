# Falling Pizza Sprite
# Demonstrates a moving sprite
# Michael Dawson 5/10/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Pizza(games.Sprite):
    """ A falling pizza. """
    def __init__(self, screen, x, y, image, dx, dy):
        """ Initialize pizza object. """
        self.init_sprite(screen = screen, x = x, y = y,
                         image = image, dx = dx, dy = dy)

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = 0)
my_screen.set_background(wall_image)

pizza_image = games.load_image("pizza.bmp")
Pizza(screen = my_screen, x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
      image = pizza_image, dx = 0, dy =1)

my_screen.mainloop()

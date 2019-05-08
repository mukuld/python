# Slippery Pizza Program
# Demonstrates testing for sprite collisions
# Michael Dawson 5/12/03

import random
from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Pan(games.Sprite):
    """ A pan. Controlled the by mouse. """
    def __init__(self, screen, x, y, image):
        self.init_sprite(screen = screen, x = x, y = y, image = image)

    def moved(self):
        """ Move to mouse position. """
        x, y = self.screen.mouse_pos()
        self.move_to(x,y)
        self.check_collide()
 
    def check_collide(self):
        """ Check for collision with pizza. """
        if self.overlapping_objects():
            pizza = self.overlapping_objects()[0]
            pizza.handle_collide()

class Pizza(games.Sprite):
    """" A slippery pizza. """
    def __init__(self, screen, x, y, image):
        self.init_sprite(screen = screen, x = x, y = y, image = image)

    def handle_collide(self):
        """ Move to a random screen location. """
        x = random.randrange(SCREEN_WIDTH)
        y = random.randrange(SCREEN_HEIGHT)
        self.move_to(x,y)

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

x = random.randrange(SCREEN_WIDTH)
y = random.randrange(SCREEN_HEIGHT)
pizza_image = games.load_image("pizza.bmp")
Pizza(screen = my_screen, x = x, y = y, image = pizza_image)

pan_image = games.load_image("pan.bmp")
Pan(screen = my_screen,
    x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
    image = pan_image)

my_screen.mouse_visible(False)

my_screen.mainloop()

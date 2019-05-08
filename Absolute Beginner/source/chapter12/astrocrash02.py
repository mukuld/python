# Astrocrash02
# Get the ship rotating
# Michael Dawson 5/20/03

import random
from livewires import games

# global constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
THE_SCREEN = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)


class Asteroid(games.Sprite):
    """ An asteroid which floats across the screen. """
    image_big = games.load_image("asteroid_big.bmp")
    image_med = games.load_image("asteroid_med.bmp")
    image_small = games.load_image("asteroid_small.bmp")
      
    def __init__(self, screen, x, y, size):
        """ Initialize asteroid sprite. """      
        if size == 1:
            image = Asteroid.image_small
        elif size == 2:
            image = Asteroid.image_med
        elif size == 3:
            image = Asteroid.image_big
        else:
            print "Asteroid size must be 1, 2, or 3."
            sys.exit()

        # set velocity based on asteroid size
        dx = random.choice([2, -2]) * random.random() / size
        dy = random.choice([2, -2]) * random.random() / size

        self.init_sprite(screen = screen, x = x, y = y,
                         dx = dx, dy = dy, image = image)
        self.size = size

    def moved(self):
        """ Wrap the asteroid around screen. """    
        if self.get_top() > SCREEN_HEIGHT:
            self.set_bottom(0)
 
        if self.get_bottom() < 0:
            self.set_top(SCREEN_HEIGHT)

        if self.get_left() > SCREEN_WIDTH:
            self.set_right(0)

        if self.get_right() < 0:
            self.set_left(SCREEN_WIDTH)


class Ship(games.Sprite):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3      

    def __init__(self, screen, x, y):
        """ Initialize ship sprite. """
        self.init_sprite(screen = screen, x = x, y = y, image = Ship.image)

    def moved(self):
        """ Rotate the ship based on key presses. """
        # rotate based on left and right arrow keys
        if self.screen.is_pressed(games.K_LEFT):
            self.rotate_by(-Ship.ROTATION_STEP)
      
        if self.screen.is_pressed(games.K_RIGHT):
            self.rotate_by(Ship.ROTATION_STEP)


# main
my_screen = THE_SCREEN
nebula_image = games.load_image("nebula.jpg")
my_screen.set_background(nebula_image)

# create 8 asteroids
for i in range(8):
    x = random.randrange(SCREEN_WIDTH)
    y = random.randrange(SCREEN_HEIGHT)
    size = random.randrange (1, 4)
    Asteroid(screen = my_screen, x = x, y = y, size = size)

# create the ship
Ship(screen = my_screen, x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
my_screen.mainloop ()


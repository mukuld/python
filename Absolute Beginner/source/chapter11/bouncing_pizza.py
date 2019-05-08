# Bouncing Pizza
# Demonstrates dealing with moving sprites and screen boundries
# Michael Dawson 5/11/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Pizza(games.Sprite):
    """ A bouncing pizza. """
    def __init__(self, screen, x, y, image, dx, dy):
        """ Initialize pizza object. """
        self.init_sprite(screen = screen, x = x, y = y,
                         image = image, dx = dx, dy = dy)

    def moved(self):
        """ Reverse a velocity component if edge of screen reached. """
        dx, dy = self.get_velocity()
        if self.get_right() > SCREEN_WIDTH or self.get_left() < 0:
            self.set_velocity(-dx, dy)
        if self.get_bottom() > SCREEN_HEIGHT or self.get_top() < 0:
            self.set_velocity(dx, -dy)

# main
my_screen = games.Screen(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

pizza_image = games.load_image("pizza.bmp")
Pizza(screen = my_screen, x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
      image = pizza_image, dx = 1, dy =1)

my_screen.mainloop()

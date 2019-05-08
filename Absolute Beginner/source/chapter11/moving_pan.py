# Moving Pan
# Demonstrates mouse input
# Michael Dawson 5/11/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Pan(games.Sprite):
    """" A pan. Controlled by the mouse. """
    def __init__(self, screen, x, y, image):
        """ Initialize pan object. """
        self.init_sprite(screen = screen, x = x, y = y, image = image)

    def moved(self):
        """ Move pan to mouse position. """
        x, y = self.screen.mouse_pos()
        self.move_to(x,y)

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

pan_image = games.load_image("pan.bmp")
Pan(screen = my_screen,
    x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
    image = pan_image)

my_screen.mouse_visible(False)

my_screen.mainloop()

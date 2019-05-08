# Rotate Sprite
# Demonstrates rotating a sprite
# Michael Dawson 5/18/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ship(games.Sprite):
    """ A moving and rotating ship. """
    def __init__(self, screen, x, y, image):
        """ Initialize ship sprite. """
        self.init_sprite(screen = screen, x = x, y = y, image = image)

    def moved(self):
        """ Move and rotate ship based on key presses. """
        # move the ship based on key presses
        x, y = self.get_pos()
        if self.screen.is_pressed(games.K_w):
            y -= 1           
        if self.screen.is_pressed(games.K_s):
            y += 1
        if self.screen.is_pressed(games.K_a):
            x -=1
        if self.screen.is_pressed(games.K_d):
            x +=1
        self.move_to(x, y)
        
        # rotate the ship based on key presses
        if self.screen.is_pressed(games.K_LEFT):
            self.rotate_by(-1)         
        if self.screen.is_pressed(games.K_RIGHT):
            self.rotate_by(1)

        if self.screen.is_pressed(games.K_1):
            self.rotate_to(0)
        if self.screen.is_pressed(games.K_2):
            self.rotate_to(90)
        if self.screen.is_pressed(games.K_3):
            self.rotate_to(180)
        if self.screen.is_pressed(games.K_4):
            self.rotate_to(270)

         
# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("nebula.jpg", transparent = False)
my_screen.set_background(wall_image)

ship_image = games.load_image("ship.bmp")
Ship(screen = my_screen,
     x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2,
     image = ship_image)

my_screen.mainloop()

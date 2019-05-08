# Pizza Panic
# Player must catch falling pizzas before they hit the ground
# Michael Dawson 5/12/03

import random
from livewires import games, color

SCREEN_WIDTH = 640  
SCREEN_HEIGHT = 480
THE_SCREEN = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

class Pan(games.Sprite):
    """
    A pan controlled by player to catch falling pizzas.
    """
    image = games.load_image("pan.bmp")

    def __init__ (self, screen, x, y):
        """ Initialize pan object. Create a Text object for player's score. """
        self.init_sprite(screen = screen, x = x, y = y, image = Pan.image)
        self.score_value = 0
        self.score_text = games.Text(screen = self.screen, x = 550, y = 20,
                                     text = "Score: 0", size = 25, color = color.black)

    def moved(self):
        """ Move pan to mouse x position. """
        x, y = self.screen.mouse_pos()
        self.move_to(x, self.get_ypos())
        if self.get_left() < 0:
            self.set_left(0)
        if self.get_right() > SCREEN_WIDTH:
            self.set_right(SCREEN_WIDTH)
        self.check_for_catch()

    def check_for_catch(self):
        """ Check if pan catches a pizza. """
        for pizza in self.overlapping_objects():
            self.handle_caught()
            pizza.handle_caught()

    def handle_caught(self):
        """ Increase and display score. """
        self.score_value += 10
        self.score_text.set_text("Score: " + str(self.score_value))


class Pizza(games.Sprite):
    """
    A pizza which falls to the ground.
    """ 
    image = games.load_image("pizza.bmp")
    START_Y = 90              # start any pizza at chef's chest-level
    speed = 1

    def __init__(self, screen, x):
        """ Initialize a pizza object. """
        self.init_sprite(screen = screen, x = x, y = Pizza.START_Y,
                         dx = 0, dy = Pizza.speed, image = Pizza.image)

    def moved(self):
        """ Check if a pizza's bottom edge has reached screen bottom. """
        if self.get_bottom() > SCREEN_HEIGHT:
            self.game_over()

    def handle_caught(self):
        """ Destroy self if caught. """
        self.destroy()

    def game_over(self):
        """ End the game. """
        # destroy all game objects except the Text object (player's score)
        for game_object in self.screen.all_objects():
            if not isinstance(game_object, games.Text):
                game_object.destroy()
                
        # show 'Game Over' for 250 mainloop() cycles (at 50 fps that's 5 seconds)
        games.Message(screen = self.screen,
                      x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
                      text = "Game Over", size = 90, color = color.red,
                      lifetime = 250, after_death = self.screen.quit)


class Chef(games.Sprite):
    """
    A chef which moves left and right, dropping pizzas.
    """
    image = games.load_image("chef.bmp")
    Y = 55                    # put the chef right on the top of the brick wall

    def __init__ (self, screen, x, speed, odds_change):
        """ Initialize the Chef object. """
        self.init_sprite(screen = screen, x = x, y = Chef.Y,
                         dx = speed, dy = 0, image = Chef.image)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def moved(self):
        """ Determine if direction needs to be reversed. """
        if self.get_left() < 0 or self.get_right() > SCREEN_WIDTH:
            self.reverse()
        else:
            same_direction = random.randrange(self.odds_change)
            if not same_direction:
                self.reverse()
        self.drop_pizza()

    def reverse(self):
        """ Reverse direction. """
        dx, dy = self.get_velocity()
        self.set_velocity((-dx, dy))

    def drop_pizza(self):
        """ Decrease countdown or drop pizza and reset countdown. """
        if self.time_til_drop:
            self.time_til_drop -= 1
        else:
            # set so buffer will be 15 pixels, regardless of pizza speed
            self.time_til_drop = int(65 / Pizza.speed)
            Pizza(self.screen, self.get_xpos())


def main():      
    my_screen = THE_SCREEN
    my_screen.mouse_visible(False)
    wall_image = games.load_image("wall.jpg", transparent = False)
    my_screen.set_background(wall_image)

    Chef(screen = my_screen, x = SCREEN_WIDTH/2, speed = 1, odds_change = 250) 
    Pan(screen = my_screen, x = SCREEN_WIDTH/2, y = 435)

    my_screen.mainloop()

# start program
main()


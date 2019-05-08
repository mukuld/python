# Astrocrash08
# Add levels, scorekeeping, and sounds
# Michael Dawson 5/22/03

# imports
import random, math
from livewires import games, color

# global constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
THE_SCREEN = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

# classes
class Wrapper(games.Sprite):
    """ A sprite that wraps around the screen. """
    def moved(self):
        """ Wrap sprite around screen. """    
        if self.get_top() > SCREEN_HEIGHT:
            self.set_bottom(0)
 
        if self.get_bottom() < 0:
            self.set_top(SCREEN_HEIGHT)

        if self.get_left() > SCREEN_WIDTH:
            self.set_right(0)

        if self.get_right() < 0:
            self.set_left(SCREEN_WIDTH)

    def die(self):
        """ Destroy self. """
        self.destroy()


class Collider(Wrapper):
    """ A Wrapper that can collide with any other Wrapper. """
    def moved(self):
        """ Destroy self and overlapping object if object is Wrapper. """
        Wrapper.moved(self)
        for game_object in self.overlapping_objects():
            if isinstance(game_object, Wrapper):
                game_object.die()
                self.die()                

    def die(self):
        """ Destroy self and leave explosion behind. """
        Explosion(self.screen, self.get_xpos(), self.get_ypos())
        self.destroy()


class Asteroid(Wrapper):
    """ An asteroid which floats across the screen. """
    image_big = games.load_image("asteroid_big.bmp")
    image_med = games.load_image("asteroid_med.bmp")
    image_small = games.load_image("asteroid_small.bmp")
    total = 0
      
    def __init__(self, screen, x, y, size):
        """ Initialize asteroid sprite. """
        Asteroid.total += 1
        
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
        
    def die(self):
        """ Destroy asteroid. """
        Asteroid.total -= 1
        Game.increase_score(30 / self.size)

        # if asteroid isn't small, replace with two smaller asteroids
        new_size = self.size - 1
        if new_size:
            for i in range(2):
                Asteroid(screen = self.screen,
                         x = self.get_xpos(), y = self.get_ypos(),
                         size = new_size)

        # if all asteroids are gone, create next level
        if not Asteroid.total:
            Game.next_level(self.screen)

        Wrapper.destroy(self)
        

class Ship(Collider):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")
    ROTATION_STEP = 3      
    VELOCITY_STEP = .03
    VELOCITY_MAX = 3
    MISSILE_DELAY = 25

    def __init__(self, screen, x, y):
        """ Initialize ship sprite. """
        self.init_sprite(screen = screen, x = x, y = y, image = Ship.image)
        self.missile_wait = 0

    def moved(self):
        """ Move the ship or fire missile based on key presses. """
        # rotate based on left and right arrow keys
        if self.screen.is_pressed(games.K_LEFT):
            self.rotate_by(-Ship.ROTATION_STEP)
      
        if self.screen.is_pressed(games.K_RIGHT):
            self.rotate_by(Ship.ROTATION_STEP)

        # apply thrust based on up arrow key
        if self.screen.is_pressed(games.K_UP):
            Ship.sound.play()
            
            # get velocity factor based on ship's angle
            angle = self.get_angle() * math.pi / 180  # convert to radians
            add_dx = Ship.VELOCITY_STEP * math.sin(angle)
            add_dy = -Ship.VELOCITY_STEP * math.cos(angle)
            
            # add current velocity and velocity change to get new velocity
            dx, dy = self.get_velocity()
            new_dx = dx + add_dx
            new_dy = dy + add_dy

            # cap velocity in each direction
            if new_dx < -Ship.VELOCITY_MAX:
                new_dx = -Ship.VELOCITY_MAX
            if new_dx > Ship.VELOCITY_MAX:
                new_dx = Ship.VELOCITY_MAX
            if new_dy < -Ship.VELOCITY_MAX:
                new_dy = -Ship.VELOCITY_MAX
            if new_dy > Ship.VELOCITY_MAX:
                new_dy = Ship.VELOCITY_MAX

            # set new velocity
            self.set_velocity(new_dx, new_dy)

        Collider.moved(self)

        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait:
            self.missile_wait -= 1

        # fire missile if spacebar pressed and enough time has elapsed            
        if self.screen.is_pressed(games.K_SPACE) and not self.missile_wait:
            Missile(self.screen, self.get_xpos(), self.get_ypos(), self.get_angle())
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """ Destroy ship and end the game. """
        self.game_over()
        Collider.die(self)

    def game_over(self):
        """ End the game. """
        # show 'Game Over' for 250 mainloop cycles (at 50 fps that's 5 seconds)
        games.Message(screen = self.screen,
                      x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
                      text = "Game Over", size = 90, color = color.red,
                      lifetime = 250, after_death = self.screen.quit)
    

class Missile(Collider):
    """ A missile launched by the player's ship. """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, screen, ship_x, ship_y, ship_angle):
        """ Initialize missile sprite. """
        Missile.sound.play()
        
        # convert to radians
        angle = ship_angle * math.pi / 180  

        # calculate missile's starting position 
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = -Missile.BUFFER * math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = -Missile.VELOCITY_FACTOR * math.cos(angle)

        # create the missile
        self.init_sprite(screen = screen, x = x, y = y,
                         dx = dx, dy = dy, image = Missile.image)
        self.lifetime = Missile.LIFETIME

    def moved(self):
        """ Move the missile. """
        # if lifetime is up, destroy the missile
        self.lifetime -= 1
        if not self.lifetime:
            self.destroy()

        Collider.moved(self)


class Explosion(games.Animation):
    """ Explosion animation. """
    sound = games.load_sound("explosion.wav")
    images = []
    for i in range(1, 10):
        file_name = "explosion" + str(i) + ".bmp"
        image = games.load_image(file_name)
        images.append(image)

    def __init__(self, screen, x, y):
        games.Animation.__init__(self, screen = screen, x = x, y = y,
                                 images = Explosion.images,
                                 n_repeats = 1, repeat_interval = 4)
        Explosion.sound.play()


class Game(object):
    """ The game itself. """
    level = 1
    sound = games.load_sound("level.wav")

    def create_ship(screen, x, y):
        Game.ship = Ship(screen = screen, x = x, y = y)

    create_ship = staticmethod(create_ship)

    def create_score(screen):
        Game.score_value = 0
        Game.score_text = games.Text(screen = screen, x = 550, y = 20,
                                text = "Score: " + str(Game.score_value),
                                size = 25, color = color.white)
        
    create_score = staticmethod(create_score)

    def increase_score(points):
        """ Increase a player's score. """
        Game.score_value += points
        Game.score_text.set_text("Score: " + str(Game.score_value))

    increase_score = staticmethod(increase_score)

    def next_level(screen):
        """ Create the next level. """
        # amount of space around ship to preserve when creating asteroids
        BUFFER = 200

        # play new level sound (except at first level)
        if Game.level > 1:
            Game.sound.play()
        
        # create new asteroids 
        for i in range(Game.level):
            # pick random x and y at least BUFFER distance from ship's x and y
            while True:
                x = random.randrange(SCREEN_WIDTH)
                y = random.randrange(SCREEN_HEIGHT)
                x_dist = abs(Game.ship.get_xpos() - x)
                y_dist = abs(Game.ship.get_ypos() - y)
                if x_dist + y_dist > BUFFER:
                    break           

            # create the asteroid
            Asteroid(screen = screen, x = x, y = y, size = 3)
            
        # display level number
        games.Message(screen = screen,
                      x = SCREEN_WIDTH / 2, y = 50,
                      text = "Level " + str(Game.level),
                      size = 40, color = color.yellow, lifetime = 150)
            
        Game.level += 1

    next_level = staticmethod(next_level)
   

# main
def main():
    my_screen = THE_SCREEN
    nebula_image = games.load_image("nebula.jpg")
    my_screen.set_background(nebula_image)

    games.load_music("theme.mid")
    games.play_music(-1)

    Game.create_ship(screen = my_screen, x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    Game.create_score(screen = my_screen)
    Game.next_level(screen = my_screen)

    my_screen.mainloop()


# start program
main()

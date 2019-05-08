# Astrocrash07
# Add explosions
# Michael Dawson 5/20/03

import random
import math
from livewires import games

# global constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
THE_SCREEN = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)


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

    def die(self):
        """ Destroy asteroid. """
        # if asteroid isn't small, replace with two smaller asteroids
        new_size = self.size - 1
        if new_size:
            for i in range(2):
                Asteroid(screen = self.screen,
                         x = self.get_xpos(), y = self.get_ypos(),
                         size = new_size)
        Wrapper.die(self)


class Ship(Collider):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25

    def __init__(self, screen, x, y):
        """ Initialize ship sprite. """
        self.init_sprite(screen = screen, x = x, y = y, image = Ship.image)
        self.missile_wait = 0

    def moved(self):
        """ Rotate the ship based on key presses. """
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

            # set new velocity
            self.set_velocity(new_dx, new_dy)

        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait:
            self.missile_wait -= 1

        # fire missile if spacebar pressed and enough time has elapsed     
        if self.screen.is_pressed(games.K_SPACE) and not self.missile_wait:
            Missile(self.screen, self.get_xpos(), self.get_ypos(), self.get_angle())
            self.missile_wait = Ship.MISSILE_DELAY

        Collider.moved(self)
  

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
    
my_screen.mainloop()


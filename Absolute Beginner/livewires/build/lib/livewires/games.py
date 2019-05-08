###############################################################################
### Games support module for LiveWires using pygame. 
### 
### $Revision: 1.7 $ -- $Date: 2001/10/27 17:43:51 $ 
############################################################################### 
# Copyright Richard Crook, Gareth McCaughan, Rhodri James, Neil Turton
# and Paul Wright.  All rights reserved. 
#  
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: 
#  
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer. 
#  
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution. 
#  
# Neither name of Scripture Union nor LiveWires nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission. 
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL SCRIPTURE UNION
# OR THE CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 
############################################################################### 
###############################################################################
# Modified by Michael Dawson
# 11/30/02
#
#  Deleted classes 
#
#  Renamed class 'Object' to 'Games_Object' to aviod confusion with newly
#  introduced 'object'
#
#  Games_Object Class
#       - made all objects moveable
#       - prefixed methods pos(), xpos(), ypos(), bbox(), angle() with 'get_'
#       - added methods get_top(), get_ bottom(), get_left() and get_right()
#         which return an object's top, bottom, left and right coordinates,
#         respectively
#       - added methods set_left(), set_right(), set_top(), set_bottom() which
#         set an object's left, right, top, bottom coordinates, respectively
#
#  Animation Class
#       - Class now receives only one list of images to animate
#       - images now displayed in order, from first frame to last (and not the
#         reverse)
#       - n_repeats parameter now represents the number of complete cycles to
#         display (and not the number of frames)
#
#  Added functions for pygame.music.mixer access
#
#  "Americanized" the spelling of color: 'colour' -> 'color'
#
#
###############################################################################
 
import pygame, pygame.image, pygame.mixer, pygame.font, pygame.transform 
import pygame.draw 
from pygame.locals import * # Richard's going to love this... 
 
pygame.init () 
 
 
############################################################################### 
## Error classes ############################################################## 
############################################################################### 
 
class GamesError (Exception): pass 
 
############################################################################### 
## Screen class ############################################################### 
############################################################################### 
##                                           
## The Screen object represents the playing area. Since we can have  
## only one screen under pygame, it's just a handy container for stuff 
## 
############################################################################### 
 
class Screen: 
 
    initialised = 0 
 
    def __init__ (self, width=640, height=480): 
 
        self.init_screen (width, height) 
 
    def init_screen (self, width=640, height=480): 
        """ 
        width -- width of graphics window 
        height -- height of graphics window 
        """ 
 
        # Bomb if you try this more than once: pygame can only have one 
        # window 
        if Screen.initialised: 
            raise GamesError, "Cannot have more than on Screen object" 
         
        Screen.initialised = 1 
         
        # Create the pygame display 
        self._display = pygame.display.set_mode ((width, height), HWSURFACE)
        self._width = width  
        self._height = height
        self._background = self._display.convert () 
 
        # Initialise a list of objects in play 
        self._objects = [] 
        # Initialise list dirty rectangles to be repainted 
        self._dirtyrects = [] 
 
        # Time when we should draw the next frame 
        self._next_tick = 0 
 
    def is_pressed (self, key): 
        return pygame.key.get_pressed () [key]

    def mouse_pos(self):
        return pygame.mouse.get_pos()

    def mouse_visible(self, v):
        pygame.mouse.set_visible(v)
 
    def set_background (self, background): 
        """ 
        Set the background to the surface provided. Note that the  
        surface should not have transparency set, or weird things 
        will happen. 
        """ 
 
        self._background = pygame.Surface((self._width, self._height)) 
        for x in range(0, self._width, background.get_width()): 
            for y in range (0, self._height, background.get_height()): 
                self._background.blit(background, (x, y)) 
                 
        self._display.blit (self._background, (0,0)) 
        pygame.display.update () 
 
    def tick (self): 
        """ 
        If you override the tick method in a subclass of the Screen 
        class, you can specify actions which are carried out every 
        tick. 
        """ 
        pass

    def keypress(self, key):
        """
        If you override the keypress method, you will be able to
        handle individual keypresses instead of dealing with the
        keys held down as in the standard library
        """

        pass

    def handle_events (self):
        """
        If you override this method in a subclass of the Screen
        class, you can specify how to handle different kinds of
        events.  However you must handle the quit condition!
        """
        events = pygame.event.get ()
        for event in events:
            if event.type == QUIT:
                self.quit ()
            elif event.type == KEYDOWN:
                self.keypress (event.key)
 
    def quit (self): 
        """ 
        Calling this method will stop the main loop from running and 
        make the graphics window disappear. 
        """ 
             
        self._exit = 1 
 
    def clear (self):
        """
        Destroy all objects on this Screen.
        """
        for object in self._objects[:]:
            object.destroy ()
        self._objects = []
 
    def _update_display (self):
        """
        Get the actual display in sync with reality.
        """
        pygame.display.update (self._dirtyrects)
        self._dirtyrects = []

    def mainloop (self, fps = 50): 
        """ 
        Run the pygame main loop. This will animate the objects on the 
        screen and call their tick methods every tick. 
 
        fps -- target frame rate 
        """ 
 
        self._exit = 0 
 
        while not self._exit: 
            self._wait_frame (fps) 
 
            for object in self._objects: 
                object._erase ()

            # Take a copy of the _objects list as it may get changed in place. 
            for object in self._objects [:]: 
                if object._tickable: object._tick () 
 
            self.tick () 
 
            for object in self._objects: 
                object._draw () 
 
            self._update_display()

            self.handle_events() 
 
        # Throw away any pending events.
        pygame.event.get()
 
    def _wait_frame (self, fps): 
        "Wait for the correct fps time to expire" 
        this_tick = pygame.time.get_ticks() 
        if this_tick < self._next_tick: 
            pygame.time.delay(int(self._next_tick+0.5) - this_tick) 
        self._next_tick = this_tick + (1000./fps) 
 
    def overlapping_objects (self, rectangle): 
        """ 
        Returns a list of all the objects which overlap the rectangle 
        given. 
        """ 

        rect = pygame.Rect (rectangle)

        rect_list = []
        for obj in self._objects:
            rect_list.append (obj._rect)

        indices = rect.collidelistall (rect_list)

        over_objects = [] 
        for index in indices: 
            over_objects.append (self._objects [index]) 

        return over_objects

    ## Object list (all represented objects) 
 
    def all_objects (self): 
        """ 
        Returns a list of all the Games_Objects on the Screen. 
        """ 
        return self._objects [:]

    def _raise(self, it, above=None):
        """
        Raise an object to the top of the stack, or above the specified
        object.
        """
        # This makes sure we're always in a consistent state.
        objects = self._objects[:]
        # Remove the object from the list.
        objects.remove(it)
        if above == None:
            # Put it on top (the end).
            objects.append(it)
        else:
            # Put the object after <above>.
            idx = 1+objects.index(above)
            objects[idx:idx]=[it]
        # Install the new list.
        self._objects = objects

    def _lower(self, object, below=None):
        """
        Lower an object to the bottom of the stack, or below the specified
        object.
        """
        # This makes sure we're always in a consistent state.
        objects = self._objects[:]
        objects.remove(it)
        if below == None:
            # Put the object on the beginning (bottom) of the list.
            self._objects = [it]+objects
        else:
            # Put the object before (below) the aboject.
            idx = objects.index(below)
            objects[idx:idx]=[it]
            self._objects = objects

    def add_object (self, object):
        self._objects.append (object)
      
    def remove_object (self, object):
        try:
            self._objects.remove (object)
        except ValueError:
            # Already done it: happens in some games, not an error.
            pass

    def blit_and_dirty (self, source_surf, dest_pos):
        """
        You probably won't need to use this method in your own programs,
        as |Games_Object| and its sub-classes know how to draw themselves on
        the screen. You'd need to use method if you wanted to draw an
        image on the screen which wasn't an |Games_Object|.

        This method blits (draws, taking account of transparency) the
        given source surface |source_surf| to the screen at the position
        given by |dest_pos|. 

        It then remembers the place where the surface was drawn as
        ``dirty''.  This means that when the display is updated on the
        next tick, this part of it will be redrawn. 
        """

        rect = self._display.blit (source_surf, dest_pos) 
        self._dirtyrects.append (rect)


    def blit_background (self, rect):
        """
        This method draws the background over the given rectangle, and
        marks that rectangle as ``dirty'' (see the |blit_and_dirty|
        method for what that means). It's used to erase an object before
        moving it. You shouldn't need to call it yourself.
        """

        rect = self._display.blit (self._background, rect, rect)
        self._dirtyrects.append (rect)
         
########################################################################### 
 
## XXX Mouse handling is not currently implemented, since the correct 
## XXX interface is still non-obvious. Do we want button-press, -release 
## XXX or mouse motion events? Which should be passed to the user? The 
## XXX answer is rather application-specific... 
 
########################################################################### 

############################################################################### 
## Games_Object class #########################################################
############################################################################### 
##                                                                           ## 
## Games_Object represents a graphical object on the screen. Games_Objects   ## 
## can be moved, rotated, deleted, and maybe have other things done to them. ## 
##                                                                           ## 
############################################################################### 

class Games_Object: 
 
    def __init__ (self, screen, x, y, surface, a=0, dx=0, dy=0, da=0, interval = 1): 
        """ 
        Initialise the object:  
 
        screen -- screen object to put the object on 
        x -- x pos of centre of object's rectangle 
        y -- y pos of centre of object's rectangle 
        surface -- pygame.Surface object
        a -- inital angle of rotation
        dx -- velocity in x direction
        dy -- velocity in y direction
        da -- angular velocity
        interval -- tick() interval
        """ 
 
        self.screen = screen 
        self.screen.add_object (self) 
        self._surface = surface 
        self._orig_surface = surface # The surface before rotation 
 
        self._rect = self._surface.get_rect () 
        self.move_to (x,y) 
 
        self._a = a 
        if self._a != 0: 
            self._rotate () 
 
        self._gone = 0

        self.set_velocity (dx, dy) 
        self.set_angular_speed (da)

        self._interval = interval 
        self._tickable = 1 
        self._next = 0


    # When an object is GCed, it should disappear.
    def __del__(self):
        if not self._gone: self.destroy()

    def destroy(self): 
        """ 
        Erase object from screen and remove it from the list of objects 
        maintained by games module. 
        """ 
        self._erase () 
        self.screen.remove_object (self) 
        self._gone = 1
 
    def _erase (self): 
        """ 
        Erase object from screen by blitting the background over where  
        it was. 
        """ 
        self.screen.blit_background (self._rect)
 
    def _draw (self): 
        """ 
        Draw object on screen by blitting the image onto the screen. 
        """ 
        self.screen.blit_and_dirty (self._surface, self._rect)
 
    def replace_image(self, surface): 
        """ 
        Remove the current surface defining the object and replace 
        it with a new one.  
        """ 
        self._orig_surface = surface 
 
        if self._a != 0: 
            self._rotate () 
        else: 
            self._replace (surface) 
 
    def _replace (self, surface): 
        (x, y) = self.get_pos () 
        self._surface = surface 
        self._rect = self._surface.get_rect() 
        self.move_to (x, y) 
 
    def get_pos(self):      return (self._x, self._y) 
    def get_xpos(self):     return self._x 
    def get_ypos(self):     return self._y 
    def get_bbox(self):     return tuple(self._rect)
    def get_angle(self):    return self._a % 360
    def get_top(self):      return self._rect.top
    def get_bottom(self):   return self._rect.bottom
    def get_left(self):     return self._rect.left
    def get_right(self):    return self._rect.right

    def set_velocity (self, dx, dy=None): 
        if dy is None: dx, dy = dx 
        self._dx = dx 
        self._dy = dy 
 
    def set_angular_speed (self, da): 
        self._da = da 

    def get_angular_speed (self):
        return self._da
 
    def get_velocity (self): 
        return (self._dx, self._dy) 

    def move_to(self, x, y=None): 
        """ 
        Move the centre of the object's rectangle to the given position. 
        """ 
        # Split a supplied coordinate pair, if required 
        if y is None: x, y = x # assumed a 2-tuple 
        self._x = x 
        self._y = y 
        self._rect.centerx = int (x)
        self._rect.centery = int (y) 
     
    def move_by(self, x, y=None): 
        if y is None: x, y = x 
        x = self._x + x 
        y = self._y + y 
        self.move_to (x, y)

    def moved(self):
        pass

    def set_left(self, left):
        self._rect.left = left
        self._x = self._rect.centerx

    def set_right(self, right):
        self._rect.right = right
        self._x = self._rect.centerx

    def set_top(self, top):
        self._rect.top = top
        self._y = self._rect.centery

    def set_bottom(self, bottom):
        self._rect.bottom = bottom
        self._y = self._rect.centery
 
    def rotate_to(self, angle): 
        self._a = angle % 360 
        self._rotate() 
         
    def rotate_by(self, angle): 
        self.rotate_to(self._a+angle) 
 
    def _rotate(self): 
        self._replace (pygame.transform.rotate (self._orig_surface, -self._a)) 
 
    def _tick (self):
        self._next = self._next + 1 
        if self._next >= self._interval: 
            self._next = 0  
            self.tick ()
        if self._dx or self._dy:
            self.move_by(self._dx, self._dy) 
        if self._da: 
            self.rotate_by(self._da) 
        self.moved () 

    def tick(self):
        pass
 
    def get_interval (self):
        return self._interval

    def set_interval (self, interval):
        self._interval = interval
 
    def stop (self): 
        self._tickable = 0 
 
    def start (self): 
        self._tickable = 1 
        self._next = 0 
    
    def overlapping_objects(self): 
        objects = self.screen.overlapping_objects(self._rect)
        if self in objects:
            objects.remove (self)
        return objects
   
    def overlaps(self, object): 
        return self._rect.colliderect(object._rect) 
     
    def raise_object(self, above=None):
        """
        Raise an object to the top of the stack, or above the specified
        object.
        """
        self.screen._raise(self, above)
     
    def lower_object(self, below=None):
        """
        Lower an object to the bottom of the stack, or below the specified
        object.
        """
        self.screen._lower(self, below)
  
 
class Text(Games_Object): 
    """ 
    A class for representing text on the screen. 
    """ 
     
    def __init__(self, screen, x, y, text, size, color, a=0, dx=0, dy=0, da=0, interval = 1): 
         
        self.init_text (screen, x, y, text, size, color, a, dx, dy, da, interval) 
 
    def init_text (self, screen, x, y, text, size, color, a, dx, dy, da, interval): 
        self._size = size 
        self._color = color 
        self._text = text 
        self._font = pygame.font.Font(None, self._size) 
        Games_Object.__init__(self, screen, x, y, self._create_surface (), a, dx, dy, da,
                              interval) 
 
    def _create_surface (self): 
        return self._font.render(self._text, 1, self._color) 
 
    def set_text(self, text): 
        if text != self._text: 
            self._text = text 
            surface = self._create_surface () 
            self.replace_image(surface) 
 
    def get_text(self): 
        return self._text

    def set_color(self, color): 
        if color != self._color: 
            self._color = color 
            surface = self._create_surface () 
            self.replace_image(surface) 
         
    def get_color(self): 
        return self._color 


class Message(Text):

    def __init__ (self, screen, x, y, text, size, color,
                  a=0, dx=0, dy=0, da=0,
                  lifetime=0, after_death=None):
        self.init_message (screen, x, y, text, size, color,
                           a, dx, dy, da,
                           lifetime, after_death)

    def init_message (self, screen, x, y, text, size, color,
                      a, dx, dy, da,
                      lifetime, after_death=None):
        self._after_death = after_death
        self.init_text (screen, x, y, text, size, color,
                        a, dx, dy, da, lifetime)

    def tick (self):
        if self._after_death:
            self._after_death ()
        self.stop ()
        self.destroy ()


class Sprite (Games_Object): 
    """ 
    The class which lets you create sprites. 
    """ 

    def __init__ (self, screen, x, y, image, a=0, dx=0, dy=0, da=0, interval = 1):
        self.init_sprite (screen, x, y, image, a, dx, dy, da, interval)
 
    def init_sprite (self, screen, x, y, image, a=0, dx=0, dy=0, da=0, interval = 1): 
        Games_Object.__init__ (self, screen, x, y, image, a, dx, dy, da, interval)


class Animation(Sprite):
    """
    An image that changes every repeat_interval ticks.
    The n_repeats parameter is the number of complete animation cycles to show.
    If n_repeats is <= 0, the animation will repeat forever.
    You can give lists of filenames instead of lists of images, if you like.
    """

    def __init__(self, screen, x, y, images, a=0, dx=0, dy=0, da=0,
                 repeat_interval=1, n_repeats=0):
        
        self.init_animation(screen, x, y, images, a, dx, dy, da, n_repeats, repeat_interval)

    def init_animation(self, screen, x, y, images, a, dx, dy, da, n_repeats, repeat_interval):
        
        if images and type(images[0]) is type(""):
	    images = load_animation(images)
	    
        self.images = images
      	if self.images == []:
	    raise GamesError, "An animation with no images is illegal."

	self.n_repeats = n_repeats or -1
	if self.n_repeats > 0:
            self.n_repeats = (self.n_repeats * len(self.images))
            
        first_image = self.next_image()
        
        Games_Object.__init__(self, screen, x, y, self.next_image(),
                              a, dx, dy, da, repeat_interval)
 
    def next_image(self):
        if self.n_repeats==0: return None
        if self.n_repeats>0: self.n_repeats -= 1
        new_image = self.images[0]
        self.images = self.images[1:] + [self.images[0]]
        return new_image

    def tick(self):
        new_image = self.next_image()
	if new_image is None: self.destroy()
        else: self.replace_image(new_image)


############################################################################### 
## Utility functions 
############################################################################### 
def load_image(file_name, transparent=1): 
    """Loads an image, prepares it for play. Returns a pygame.Surface object 
    which you can give as the "image" parameter to Games_Object. 
 
    file_name -- the filename of the image to load 
    transparent -- whether the background of the image should be transparent. 
                   Defaults to true. 
                   The background color is taken as the color of the pixel 
                   at (0,0) in the image. 
    """ 
    try: 
        surface = pygame.image.load(file_name) 
    except pygame.error: 
        raise GamesError, 'Could not load image "%s" %s'%(file_name, pygame.get_error()) 
    if transparent: 
        corner = surface.get_at((0, 0)) 
        surface.set_colorkey(corner, RLEACCEL) 
    return surface.convert()

def scale_image(image, x_scale, y_scale=None):
    if y_scale is None: y_scale = x_scale
    (x_size, y_size) = image.get_size()
    x_size = x_size * x_scale
    y_size = y_size * y_scale
    return pygame.transform.scale (image, (x_size, y_size))

def load_animation(file_names, transparent=1):
    """
    Loads a number of files.  Receives file names.  Returns corresponding file objects
    needed by the Animation constructor.
    """
    def _(name, transparent=transparent):
        try: surface = pygame.image.load(name)
	except pygame.error:
	    raise GamesError, 'Could not load animation frame "%s": %s' % (
	        name, pygame.get_error())
        if transparent:
	    surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)
	return surface.convert()
    files = map(_, file_names)
    return files
 
def load_sound(file_name): 
    """ 
    Load a sound file, returning a Sound object. 
    """ 
    return pygame.mixer.Sound(file_name)

def load_music(file_name):
    """ 
    Loads music from a file file. 
    """ 
    pygame.mixer.music.load(file_name)

def play_music(loop = 0):
    """ 
    Plays the current music.
    """ 
    pygame.mixer.music.play(loop)

def fade_out_music(millisec):
    """ 
    Fades out the current music in millisec milliseconds.
    """ 
    pygame.mixer.music.fadeout(millisec)

def stop_music():
    """ 
    Stops the current music.
    """ 
    pygame.mixer.music.stop()

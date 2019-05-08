# Explosion
# Demonstrates creating an animation
# Michael Dawson 5/19/03

from livewires import games

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

nebula_image = games.load_image("nebula.jpg", transparent = 0)
my_screen.set_background(nebula_image)

explosion_files = ["explosion1.bmp",
                   "explosion2.bmp",
                   "explosion3.bmp",
                   "explosion4.bmp",
                   "explosion5.bmp",
                   "explosion6.bmp",
                   "explosion7.bmp",
                   "explosion8.bmp",
                   "explosion9.bmp"]
          
games.Animation(screen = my_screen,
                x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
                images = explosion_files,
                n_repeats = 0, repeat_interval = 5)

my_screen.mainloop()

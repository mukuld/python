# Big Score
# Demonstrates displaying text on a graphics screen
# Michael Dawson 5/9/03

from livewires import games, color

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

games.Text(screen = my_screen, x = 500, y = 30,
           text = "Score: 1756521", size = 50, color = color.black)

my_screen.mainloop()

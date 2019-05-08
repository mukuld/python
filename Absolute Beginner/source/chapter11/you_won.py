# You Won
# Demonstrates displaying a temporary message on a graphics screen
# Michael Dawson - 5/9/03

from livewires import games, color

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# main
my_screen = games.Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

wall_image = games.load_image("wall.jpg", transparent = False)
my_screen.set_background(wall_image)

games.Text(screen = my_screen, x = 500, y = 30,
           text = "Score: 1756521", size = 50, color = color.black)

games.Message(screen = my_screen, x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,
              text = "You won!", size = 100, color = color.red,
              lifetime = 250, after_death = my_screen.quit)
           
my_screen.mainloop()

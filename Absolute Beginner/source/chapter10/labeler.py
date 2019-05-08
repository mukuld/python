# Labeler
# Demonstrates a label
# Michael Dawson - 6/5/03

from Tkinter import *

# create the root window
root = Tk()
root.title("Labeler")
root.geometry("200x50")

# create a frame in the window to hold other widgets
app = Frame(root)
app.grid()

# create a label in the frame
lbl = Label(app, text = "I'm a label!")
lbl.grid()

# kick off the window's event loop
root.mainloop()

# Click Counter
# Demonstrates binding an event with an event handler
# Michael Dawson - 6/6/03

from Tkinter import *

class Application(Frame):
    """ GUI application which counts button clicks. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0    # the number of button clicks
        self.create_widget()

    def create_widget(self):
        """ Create button which displays number of clicks. """
        self.bttn = Button(self)
        self.bttn["text"]= "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
          
# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()

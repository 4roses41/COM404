# * imports the whole file
from tkinter import *

# as the class inherrits from the Tk class you put TK in to the Brackets
class Gui(Tk):

    # this will open the initial window
    def __init__(self):
        super().__init__()
        
        
        
        # set window attributes
        self.title("GUI")
        self.configure(bg="#eee", height= 500, width=500)
        
        
        
        # add window components by
        #...creating an object of the component stored in an attribute
        self.heading_label = Label()
        self.heading_label.place(x=0, y=0)
        # ...setting the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 24", text= "This is a Heading")
        

        
        # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)
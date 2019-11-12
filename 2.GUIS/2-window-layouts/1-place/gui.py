from tkinter import *

class Gui(Tk):
    #this is the function to open the window
    def __init__(self):
        super().__init__()

        #these are the attributes of the window
        self.title("Newsletter")
        self.configure(bg="grey", height= 200, width= 350)

        #add the call to the function to make up the newsletter box
        self.add_frame_box()
        self.add_heading_label()
        self.add_main_message()
        self.add_email_text()
        self.add_entry_box()
        self.add_subscribe_box()

    # this is the function to create a label within the window
    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.place(x=35, y=20)
        #this is how the window will look
        self.heading_label.configure(font="Arial 15", text="RECEIVE OUR NEWSLETTER")
        
    def add_main_message(self):
        self.main_message = Label()
        self.main_message.place(x=13, y=80)
        #this is how the message will look
        self.main_message.configure(font="Arial 10", text= "Please enter your email below to receive our newsletter.")
    
    def add_email_text(self):
        self.email_text = Label()
        self.email_text.place(x=35, y=135)
        #this is how the text will look
        self.email_text.configure(font="Arial 10", text="Email:")
        
    def add_entry_box(self):
        self.entry_box = Entry()
        self.entry_box.place(x=80, y=135)
        self.entry_box.configure(font= "Arial 10", width=32 )
    
    def add_frame_box(self):
        self.frame_box = Frame()
        self.frame_box.place(x=10 , y=10)
        self.frame_box.configure(height= 180, width= 330)
    
    def add_subscribe_box(self):
        self.subscribe_box = Button()
        self.subscribe_box.place(x= 100, y=160 )
        self.subscribe_box.configure(height= 1, width=20, text= "Subscribe", bg= "grey")







from tkinter import *
from tkinter import messagebox


class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        self.configure(height = 250, width= 350)
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
        
    def __add_heading_label(self):
        self.headinglabel = Label()
        self.headinglabel.configure(text = "Enterance Ticket", font = "arial 30")
        self.headinglabel.grid(row = 0, column = 0)
        
    def __add_instruction_label(self):
        self.instructionlabel = Label()
        self.instructionlabel.configure(text = "How Many Tickets are needed?", font = "arial 24" )
        self.instructionlabel.grid(column = 0, row=1)

    def __add_tickets_entry(self):
        self.ticketsentry = Entry()
        self.ticketsentry.configure(width = 20, font = "Arial 24")
        self.ticketsentry.grid(row = 3, column = 0)
        
    def __add_buy_button(self):
        self.buybutton = Button()
        self.buybutton.configure(text = "Buy", font = "arial 24")
        self.buybutton.grid(row = 4, column = 0)
        self.buybutton.bind("<ButtonRelease-1>", self.__buy_button_clicked)
    
    def __buy_button_clicked(self, event):
        num_tickets = self.ticketsentry.get()
        messagebox.showinfo("Purchased!", "You have purchased " + num_tickets + " tickets!")


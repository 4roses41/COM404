from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.configure(bg="#ffe8e8",height = 1000, width = 1000)

        self._add_main_frame()
        self._heading_label()
        self._ammount_label()
        self._ammount_input_box()
        self._clear_button()
        self._convert_button()
        self._system_message_box()
        self._system_message()             
        
    def _add_main_frame(self):
        self.add_main_frame = Frame()
        self.add_main_frame.configure(height = 800, width = 800,bg="#ffe8e8")
        self.add_main_frame.pack(pady=10, padx=10)

    def _heading_label(self):
        self.heading_label = Label(self.add_main_frame)
        self.heading_label.configure(bg="#ffe8e8",font = "arial 25", text = "Currency Converter")
        self.heading_label.grid(row = 0,column = 0, columnspan = 4)
    
    def _ammount_label(self):
        self.ammount_label = Label(self.add_main_frame)
        self.ammount_label.configure(bg="#ffe8e8",text = "Amount", font = "arial 15")
        self.ammount_label.grid(row = 1, column = 1)
    
    def _ammount_input_box(self):
        self.ammount_input_box = Entry(self.add_main_frame)
        self.ammount_input_box.configure(width = 20, font = "arial 15")
        self.ammount_input_box.grid(row = 2, column = 1, columnspan = 2)

    def _clear_button(self):
        self.clear_button = Button(self.add_main_frame)
        self.clear_button.configure(text = "Clear", font = "arial 15")
        self.clear_button.grid(row=3, column =1, pady= 10)
        self.clear_button.bind("<ButtonRelease-1>", self._clear_button_clicked)

    def _convert_button(self):
        self.convert_button = Button(self.add_main_frame)
        self.convert_button.configure(text = "Convert", font = "arial 15")
        self.convert_button.grid(row=3, column =2,pady= 10)
        self.convert_button.bind("<ButtonRelease-1>", self._convert_button_clicked)

    def _system_message_box(self):
        self.system_message_box = Frame(self.add_main_frame)
        self.system_message_box.configure(height = 400,width = 400,bg = "#fffbce")
        self.system_message_box.grid(row = 4, column =0, columnspan= 4,)
    
    def _system_message(self):
        self.system_message = Label(self.system_message_box)
        self.system_message.configure(bg = "#fffbce",text = "System Message Displayed Here")
        self.system_message.pack(pady=30, padx=40)            
    
    def _convert_button_clicked(self,event):
        self.system_message.configure(bg = "#fffbce",text = "Converting...")
        self.system_message.pack(pady=30, padx=90)

    def _clear_button_clicked(self,event):
        self.system_message.configure(bg = "#fffbce",text = "System Message Displayed Here")
        self.system_message.pack(pady=30, padx=40)
        self.ammount_input_box.delete(0, 'end')


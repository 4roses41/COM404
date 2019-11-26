from tkinter import *


class Gui(Tk):
    def __init__(self):
        super().__init__()

        #Images
        self.cacti_image_1 = PhotoImage(file = "cacti1.gif")
        self.cacti_image_2 = PhotoImage(file = "cacti2.gif")


        self.title("Gui")

        self.add_cactus_label()
        self.add_cacti_image_label()
        self.add_flip_button()

        
    def add_cactus_label(self):
        self.cactus_label = Label()
        self.cactus_label.grid(row = 0, column = 0)
        self.cactus_label.configure(text = "CACTUS FLIPER", font = "arial 24")

    def add_cacti_image_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1, column = 0)
        self.cacti_image_label.configure(image = self.cacti_image_1,width = 500, height = 500)

    
    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row = 2, column = 0)
        self.flip_button.configure(text = "Flip", font = "arial 20")
        self.flip_button.bind("<ButtonRelease-1>", self._button_clicked_L)
        self.flip_button.bind("<ButtonRelease-3>", self._button_clicked_R)
        

    def _button_clicked_L(self, event):
        self.cacti_image_label.configure(image = self.cacti_image_1)
        
    def _button_clicked_R(self, event):
        self.cacti_image_label.configure(image = self.cacti_image_2)
        
        

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()


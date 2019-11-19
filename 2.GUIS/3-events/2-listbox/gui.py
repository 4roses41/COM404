from tkinter import *
from tkinter import messagebox


class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Song Maker")
        self.configure(width = 400, height = 400)
        self.__add_heading()
        self.__add_lyrictoadd_label()
        self.__add_frame()
        self.__add_lyric_enter()
        self.__add_lyric_box()
        self.__add_lyric_label()

        
    def __add_heading(self):
        self.heading = Label()
        self.heading.configure(font = "arial 30", text = "Song Maker")
        self.heading.grid(padx = (100,100), row=0, column=0, sticky = "")
    
    def __add_lyrictoadd_label(self):
        self.lyricadd_label = Label()
        self.lyricadd_label.configure(font = "arial 20", text = "Lyric to add:")
        self.lyricadd_label.grid(row = 1, column = 0, sticky = W, padx=(10,0) )

    def __add_frame(self):
        self.addframe = Frame()
        self.addframe.grid(row=2, column = 0)
        
    def __add_lyric_enter(self):
        self.lyricenter = Entry(self.addframe)
        self.lyricenter.configure(font = "arial 20", width = 20)
        self.lyricenter.pack(side = LEFT)
    
    def __add_lyric_box(self):
        self.lyricbox = Button(self.addframe)
        self.lyricbox.configure(font = "arial 20", text = "Add")
        self.lyricbox.pack(side = RIGHT)
    
    
    def __add_lyric_label(self):
        pass
    


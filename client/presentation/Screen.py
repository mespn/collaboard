from tkinter import *
from tkinter import ttk

class Screen:
    def __init__(self, width:int, height:int, title: str):
        self.root = Tk()
        self.root.title(title)

        self.height = height
        self.width = width

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(True, True)

        self.setup_main_frame()
    
    def setup_main_frame(self):
        self.mainframe = ttk.Frame(self.root, padding="2 2 2 2")
        self.mainframe['borderwidth'] = 2
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
import sys
from tkinter import *
from tkinter import ttk

sys.path.append("../../presentation")

from .presentation import Screen

class WhiteBoard(Screen):
    def __init__(self):
        super().__init__(800,800, "Whiteboard")

        self.root.mainloop()

    
    
if __name__ == '__main__':
    wb = WhiteBoard()
"""
    Launcher Script
    Author: Gabriel Mellides
    Description: Loads the player window from PlayerWindow Class
    inside the graphics folder.
    Specs: Windows are designed using Pygubu (the files that have .ui Extension)
    Pafy module is used to
"""
import os
import tkinter
from graphics import PlayerWindow as Window


if __name__ == '__main__':
    # Create folder if not exists
    if not os.path.exists("pls_files"):
        os.makedirs("pls_files")
    # Calls the Player Window
    root = tkinter.Tk()
    app = Window.PlayerForm(root)
    root.title("PyYuMusic")
    root.resizable(False, False)
    root.mainloop()
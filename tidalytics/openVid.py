from Tkinter import *
from tkFileDialog import askopenfilename

#TO-DO: Add error handling for non-video file inputs
def openVid():
    Tk().withdraw()
    filepath = askopenfilename()
    return filepath

if __name__ == "__main__":
    openVid()
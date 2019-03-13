from tkinter import *

root = Tk()


def printName():
    print("Hello there Deniz")


theButton = Button(None, text="Click Me!", fg="Blue",
                   bg="Yellow", command=printName)
theButton.pack()

root.mainloop()

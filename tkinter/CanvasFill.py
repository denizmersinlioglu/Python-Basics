from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()


def createRect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")


createRect(50, 50, 100, 100)
createRect(150, 150, 260, 260)

root.mainloop()

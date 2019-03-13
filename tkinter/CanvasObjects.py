from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_rectangle(20, 20, 100, 270)

canvas.create_line(100, 100, 150, 180, 50, 40)

canvas.create_oval()

root.mainloop()
